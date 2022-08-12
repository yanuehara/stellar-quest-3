from stellar_sdk import Server, Keypair, TransactionBuilder, Network

keypair = Keypair.from_secret("SD464A7ZQLHJVHFMDYHGLGN33LNAE6YZHPYL5RSSLBXS4C5MDW7CURJQ")
payment_address = "GDD4VE45GWONEMCW55PTHEY6QEHORDODCTMMPZWVCSSRL534POPB2BZT"

server = Server("https://horizon-testnet.stellar.org")
quest_account = server.load_account(keypair.public_key)
base_fee = server.fetch_base_fee()

tbuilder = TransactionBuilder(
    source_account=quest_account,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee=base_fee,
)

for a in range(100):
    tbuilder.append_payment_op(payment_address, "0.000001", "XLM")

transaction = tbuilder.build()

transaction.sign(keypair)
response = server.submit_transaction(transaction)
print(response)