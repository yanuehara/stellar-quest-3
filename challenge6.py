from stellar_sdk import Server, Keypair, TransactionBuilder, Network
from png_generator import generate_data

keypair = Keypair.from_secret("SCHDSNWNVGEFUM7H6LTNTH53OLTDQTYPR2GZPTB7BHUTKTKJSIWO4ZKW")

server = Server("https://horizon-testnet.stellar.org")
quest_account = server.load_account(keypair.public_key)
base_fee = server.fetch_base_fee()

tbuilder = TransactionBuilder(
    source_account=quest_account,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee=base_fee,
)

for a in range(98):
    try:
        (first, second) = next(generate_data())

        data_name = f"{a:02d}{first}"
        tbuilder.append_manage_data_op(data_name, second)
    except StopIteration:
        break


transaction = tbuilder.build()

transaction.sign(keypair)
response = server.submit_transaction(transaction)
print(response)