class HashTable(object):

    def __init__(self, items=None):
        """Initialize this HashTable and set items if specified"""
        #starting with 10 slots
        self.slots = [[] for _ in range(10)]
        self.size = 0

    #display method of hashTable
    def display_hash(self):
        for i in range(len(self.slots)):
            print(i, end=" ")

            for j in self.slots[i]:
                print("-->", end=" ")
                print(j, end=" ")

            print()
    """Return a hash index by hashing the key and finding the remainder of the hash
    divided by the number of slots in the HashTable"""
    #hash function
    def _hash_function1(self,key_str, size):
        return sum([ord(c) for c in key_str]) % size
    #hash function only for integers keys
    def _hash_function3(self,key,size):
         return key%size

    def _get_hash_index(self, key):
        #call the hash function
        #print(self._hash_str(key) % len(self.slots))
        #return self._hash_str(key) % len(self.slots)
        if not((isinstance(key,int))):
            return self._hash_function1(key,len(self.slots))
        else:
            #convert int to str and use different hash function(we do because it it more efficient than use _hash_function3)
            return self._hash_function2(str(key),len(self.slots))


    def _hash_function2(self, string,size):
        """Return a hash of the given string."""
        hash = 5381
        for char in string[1:]:
            # (hash << 5) + hash is equivalent to hash * 33
            hash = (hash << 5) + hash + ord(char)
        return hash % size

    def get(self, key_search):
        """Return data found by given key in the HashTable,if key not found
        raise exception"""
        list_return=[]

        # get the slot the key belongs to
        # using our _get_hash_index function
        slot = self.slots[self._get_hash_index(key_search)]
        print(slot)
        for i,kv in enumerate(slot):
            print("the number of slot ", i, " the slot contains ", kv)
            key, value = kv
            print("key ", key)
            print("value ", value)
            if key == key_search:
                list_return.append((key,value))
        if(len(list_return)==0):
            raise Exception("Hash table does not contain key.")
        else:
            return list_return


    def set(self, key, value):
        """Add an item to the HashTable by key and value"""

        # get the slot where the key belongs to
        # using our _get_hash_index function
        slot = self.slots[self._get_hash_index(key)]

        # if the item isn't already in the hash table
        self.size += 1

        # append (key,value) to the end of the slot
        slot.append((key,value))

        # if load factor exceeds 0.95, resize
        if (self.size / len(self.slots)) > 0.95:
            self._resize()

    def delete(self, key_search):
        """Remove an item from the HashTable by key or raise KeyError if key
        is not found in the HashTable"""

        # get the slot the key belongs to
        # using our _get_hash_index function
        bucket = self.slots[self._get_hash_index(key_search)]
        key_exists=False
        indexes_del=[]

        # delete item or throw key error if item was not found
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == key_search:
                key_exists = True
                indexes_del.append(i)
        #indexes_del=indexes_del.reverse()
        if key_exists:
            for i in indexes_del:
                bucket[i]="None"
                #del bucket[i]
            for i in range(len(bucket)-1,-1,-1):
                print(i)
                if bucket[i]=="None":
                    del bucket[i]



            print('Key {} not found'.format(key_search))
        else:
            print('Key {} not found'.format(key_search))

    def _resize(self):
        """"Resize the HashTable by doubling the number of slots and rehashing all items"""

        # get a list of all items in the hash table
        l=self.slots

        # reset size for hash table
        self.size = 0

        # generate new slots of double current slots
        self.slots = [[] for i in range(len(self.slots) * 2)]
        for i in range(len(l)):
            for _,m in enumerate(l[i]):
                k, v = m
                self.set(k,v)
        return self.slots


"""
H=HashTable()
H.set("Arts",90)
H.set("Computer Science",12)
H.set("Literature",11)
H.set("Physics",12)
H.set("Biology",11)
H.set("Computer Science",5)
H.set("Literature",9)
H.set("Physics",3)
H.set("8",9)
H.display_hash()
print(H.get("Biology"))
H.delete("Physics")
print(H.slots)
"""
