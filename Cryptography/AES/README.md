### AES

AES performs a keyed permutation, where each input block is mapped to a unique output block, with the key determining which permutation to perform.
Since it is a symmetric key algorithm, the same key used to encrypt the plaintext can decrypt the ciphertext into the plaintext.

#### **Process**
AES begins with a starting state, which is a 4 by 4 matrix of bytes.  
Over the course of the 10 rounds, the state is repeatedly modified by a number of invertible transformations.  
Phases of AES (AES-128):
1. **Key Expansion** or **Key Schedule**  
From the initial 128 bit key, 11 seperate 128 bit round keys are derived, to be used in each "add round key" step  
2. **Initial key addition**  
_AddRoundKey_: the bytes of the first round key are XOR'd with the bytes of the state  
3. **Round** - repeated 10 times, for 9 main rounds and a final round  
  a) *SubBytes*: each byte of the state is substituted for a different byte according to a lookup table ("S-box")  
  b) _ShiftRows_: the last three rows of the state matrix are transposed - shifted over a column or two or three  
  c) _MixColumns_: matrix multiplication is performed on the columns of the state, combining the four bytes in each column. This is skipped in the final round
  d) _AddRoundKey_: the bytes of the current round key are XOR'd with the bytes of the state