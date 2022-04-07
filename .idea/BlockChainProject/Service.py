class Techf:
    id_base=[]

    # convert string to binary data
    @staticmethod
    def KeyDataToHash(data):
        binary_data=data.encode()
        return hashlib.sha256(binary_data).hexdigest()

    # generate unique user id in the range
    @staticmethod
    def id_generation():
        user_id=randint(1,1000000000)
        while user_id in Techf.id_base:
            user_id=randint(1,1000000000)
        else: Techf.id_base.append(user_id)
        return user_id

    # function for hash generating
    @staticmethod
    def dataToHash(data):
        json_data=json.dumps(data,sort_keys=True) # convert dictionary to string
        binary_data=json_data.encode() # convert string to binary data
        return hashlib.sha256(binary_data).hexdigest()

    @staticmethod
    def hash(block):
        json_data=json.dumps(block,sort_keys=True) # convert dictionary to string
        binary_data=json_data.encode() # convert string to binary data
        return hashlib.sha256(binary_data).hexdigest()