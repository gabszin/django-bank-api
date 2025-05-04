from ninja import Router
from .schemas import TransactionSchema
from django.shortcuts import get_object_or_404
from users.models import User
from rolepermissions.checkers import has_permission
from django.db import transaction as django_transaction
import requests
from django.conf import settings
from .models import Transactions
from django_q.tasks import async_task
from .tasks import send_notification


payments_router = Router()

@payments_router.post('/', response = {200: dict, 400:dict, 403:dict})
def make_transaction(request, payload: TransactionSchema):
    payer = get_object_or_404(User, id=payload.payer)
    payee = get_object_or_404(User, id=payload.payee)

    if payer.amount < payload.amount:
        return 400, {'error': 'Saldo  Insuficiente'}
    
    if not has_permission(payer, 'make_transfer'):
        return 403, {'error': 'Sem permissão para realizar transferências.'}
    
    if not has_permission(payee, 'receive_transfer'):
        return 403, {'error': 'O usuário não pode receber transferências.'}
    
    with django_transaction.atomic():
        payer.pay(payload.amount)
        payee.receive(payload.amount)

        transct = Transactions(
            amount = payload.amount,
            payer_id = payload.payer,
            payee_id = payload.payee,
        )
        payer.save()
        payee.save()
        transct.save()

        response = requests.get(settings.AUTHORIZE_TRANSFER_ENDPOINT).json()
        if response.get('status') != "success":
            raise Exception()
    
    async_task(send_notification, payer.first_name, payee.first_name, payload.amount)

    return 200, {'transaction_id': transct.id}