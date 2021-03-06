import obelisk
import os, sys

from twisted.internet import reactor

def tx_fetched(ec, tx):
    print ec, tx
    print tx.serialize().encode("hex")

def spend_fetched(ec, spend):
    print ec, spend

def txidx_fetched(ec, height, index):
    print ec, height, index

def txhashes_fetched(ec, hashes):
    print [h.encode("hex") for h in hashes]

def height_fetched(ec, height):
    print height

if __name__ == '__main__':
    client = obelisk.ObeliskOfLightClient("tcp://85.25.198.97:9091")
    tx_hash = "e9a66845e05d5abc0ad04ec80f774a7e" \
              "585c6e8db975962d069a522137b80c1d".decode("hex")
    client.fetch_transaction(tx_hash, tx_fetched)
    outpoint = obelisk.OutPoint()
    outpoint.hash = "f4515fed3dc4a19b90a317b9840c243b" \
                    "ac26114cf637522373a7d486b372600b".decode("hex")
    outpoint.index = 0
    client.fetch_spend(outpoint, spend_fetched)
    client.fetch_transaction_index(outpoint.hash, txidx_fetched)
    client.fetch_block_transaction_hashes(100000, txhashes_fetched)
    blk_hash = "000000000003ba27aa200b1cecaad478" \
               "d2b00432346c3f1f3986da1afd33e506".decode("hex")
    client.fetch_block_height(blk_hash, height_fetched)
    reactor.run()

