class Solution:

    def encode(self, strs: List[str]) -> str:
        separator='#'
        lengths = [str(len(word)) for word in strs]
        return separator.join(lengths)+"|>"+ "".join(strs)


    def decode(self, s: str) -> List[str]:

        [key,encoded] = s.split("|>")
        decoded=[]
        total=0
        if key=='' and encoded =='':
            return []
        for len in key.split("#"):
            len=int(len)
            print(len)
            if len==0:
                decoded.append("")
                continue
            decoded.append(encoded[total:total+len])
            total+=len
        return decoded
