
# coding: utf-8

# In[56]:


from stellar_base.keypair import Keypair
from stellar_base.asset import Asset
from stellar_base.operation import Payment
from stellar_base.transaction import Transaction
from stellar_base.transaction_envelope import TransactionEnvelope as Te
from stellar_base.memo import TextMemo
from stellar_base.horizon import horizon_testnet, horizon_livenet

alice_seed = 'SAZJ3EDATROKTNNN4WZBZPRC34AN5WR43VEHAFKT5D66UEZTKDNKUHOK'
bob_address = 'GDLP3SP4WP72L4BAJWZUDZ6SAYE4NAWILT5WQDS7RWC4XCUNUQDRB2A4'
CNY_ISSUER = 'GDVDKQFP665JAO7A2LSHNLQIUNYNAAIGJ6FYJVMG4DT3YJQQJSRBLQDG'
amount = '100'
# This is the new account ID (the StrKey representation of your newly
# created public key). This is the destination account.
new_account_addr = "GXXX"
Alice = Keypair.from_seed(alice_seed)
horizon = horizon_testnet() # horizon = horizon_livenet() for LIVENET

asset = Asset('CNY', CNY_ISSUER)
# create op
'''
op = Payment({
    # 'source' : Alice.address().decode(),
    'destination': bob_address,
    'asset': asset,
    'amount': amount
})
'''
op = CreateAccount({
    'destination': new_account_addr,
    'starting_balance': amount
})
# create a memo
msg = TextMemo('Buy yourself a beer !')

# get sequence of Alice
# Python 3
sequence = horizon.account(Alice.address().decode('utf-8')).get('sequence')
# Python 2
# sequence = horizon.account(Alice.address()).get('sequence')

# construct Tx
tx = Transaction(
    source = Alice.address().decode(),
    opts = {
        'sequence': sequence,
        # 'timeBounds': [],
        'memo': msg,
        # 'fee': 100,
        'operations': [
            op,
        ],
    },
)


# build envelope
#envelope = Te(tx=tx, opts={"network_id": "TESTNET"}) 
# envelope = Te(tx=tx, opts={"network_id": "PUBLIC"}) for LIVENET
# Build a transaction envelope, ready to be signed.
envelope = Te(tx=tx, opts={"network_id": "PUBLIC"})

# sign
envelope.sign(Alice)
# submit
xdr = envelope.xdr()
response = horizon.submit(xdr)


# In[54]:


print response


# In[51]:


from stellar_base.address import Address
publickey = 'GDVDKQFP665JAO7A2LSHNLQIUNYNAAIGJ6FYJVMG4DT3YJQQJSRBLQDG'
address = Address(address=publickey) # See signature for additional args
address.get() # Get the latest information from Horizon


# In[52]:


print("Balances: {}".format(address.balances))
print("Sequence Number: {}".format(address.sequence))
print("Flags: {}".format(address.flags))
print("Signers: {}".format(address.signers))
print("Data: {}".format(address.data))


# In[68]:


from stellar_base.keypair import Keypair
from stellar_base.asset import Asset
from stellar_base.operation import Payment
from stellar_base.transaction import Transaction
from stellar_base.transaction_envelope import TransactionEnvelope as Te
from stellar_base.memo import TextMemo
from stellar_base.horizon import horizon_testnet, horizon_livenet

alice_seed = 'SAZJ3EDATROKTNNN4WZBZPRC34AN5WR43VEHAFKT5D66UEZTKDNKUHOK'
bob_address = 'GDLP3SP4WP72L4BAJWZUDZ6SAYE4NAWILT5WQDS7RWC4XCUNUQDRB2A4'
CNY_ISSUER = 'GDVDKQFP665JAO7A2LSHNLQIUNYNAAIGJ6FYJVMG4DT3YJQQJSRBLQDG'
amount = '10'

Alice = Keypair.from_seed(alice_seed)
horizon = horizon_testnet() # horizon = horizon_livenet() for LIVENET

asset = Asset('CNY', CNY_ISSUER)
# create op
op = Payment({
    # 'source' : Alice.address().decode(),
    'destination': bob_address,
    'asset': asset,
    'amount': amount
})
# create a memo
msg = TextMemo('Buy yourself a beer !')

# get sequence of Alice
# Python 3
sequence = horizon.account(Alice.address().decode('utf-8')).get('sequence')
# Python 2
# sequence = horizon.account(Alice.address()).get('sequence')

# construct Tx
tx = Transaction(
    source = Alice.address().decode(),
    opts = {
        'sequence': sequence,
        # 'timeBounds': [],
        'memo': msg,
        #'fee': 100,
        'operations': [
            op,
        ],
    },
)


# build envelope
envelope = Te(tx=tx, opts={"network_id": "TESTNET"}) # envelope = Te(tx=tx, opts={"network_id": "PUBLIC"}) for LIVENET
# sign
envelope.sign(Alice)
# submit
xdr = envelope.xdr()
response = horizon.submit(xdr)


# In[69]:


response

