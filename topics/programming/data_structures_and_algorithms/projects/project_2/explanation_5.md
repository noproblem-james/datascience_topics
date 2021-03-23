## Blockchain

I believe the time complexity of a cryptographic hash like SHA256 is O(n) and the space complexity is O(1).

I had somme questions about this one:
1. Should the blocks have a notion of `previous_block` or just a `previous_hash`?
1. Should the timestamp should also be part of what is fed into the cryptohash function?
1. If we change the data of one of the blocks, should the chain rebuild itself, recalculating the hashes of all subsequent blocks?
1. Possibly a rewording of the previous question: How should validation work? That seems to be the whole point of a blockchain, but there were no requirements to that effect
