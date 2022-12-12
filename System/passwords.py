import hashlib 
# to make a new password, generate its hash with the hashPassword() function
# and replace it below
# TODO: find a better way to do this than just a variable here, maybe a file?
adminHash = 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86'
def hashPassword(password):
    return hashlib.sha512(password.encode("utf8")).hexdigest()