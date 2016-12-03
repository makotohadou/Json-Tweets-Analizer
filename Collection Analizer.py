jsonfile = 'python.json'
language = 'pt'
outputfile = 'LanguageRestrictedTweets.txt'


class CollectionAnalizer():
    collection = []
    def restrictLanguage(self, language):
        total = 0
        found = 0
        with open(jsonfile, 'r') as f:
            for line in f:
                tweet = json.loads(line)
                total += 1
                try:
                    if tweet['lang'] == language:
                        print tweet['text']
                        self.collection.append(tweet['text'])
                        found += 1
                except:
                    pass
        print total
        print found

    def writeCollectionToFile(self):
        with open(outputfile,'w') as f:
            for tweet in self.collection:
                f.write((tweet+"\n").encode('utf-8'))


 
