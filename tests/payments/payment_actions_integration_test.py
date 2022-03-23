from __future__ import absolute_import

from tests.checkout_test_utils import assert_response, retriable
from tests.payments.payments_test_utils import make_card_payment


def test_should_get_payment_actions(default_api):
    payment_response = make_card_payment(default_api, capture=True)

    payment_actions = retriable(callback=default_api.payments.get_payment_actions,
                                predicate=there_are_two_payment_actions,
                                payment_id=payment_response['id'])

    assert type(payment_actions) is list
    assert payment_actions.__len__() > 0
    for action in payment_actions:
        assert_response(action,
                        'amount',
                        'approved',
                        'processed_on',
                        'reference',
                        'response_code',
                        'response_summary',
                        'type')


def there_are_two_payment_actions(response) -> bool:
    return response.__len__() == 2