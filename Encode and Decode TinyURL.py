class Codec:
    alphabets = '1234567890' + string.ascii_letters
    def __init__(self):
        self.tinyToLong = {}
        self.longToTiny = {}
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.longToTiny:
            code = ''.join(random.choice(Codec.alphabets) for _ in range(6))
            if code not in self.tinyToLong:
                self.tinyToLong[code] = longUrl
                self.longToTiny[longUrl] = code
        return "http://tinyurl.com/"+code

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.tinyToLong[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
