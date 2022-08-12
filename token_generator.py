token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rlc3RhbmNob3Iuc3RlbGxhci5vcmcvYXV0aCIsInN1YiI6IkdCWDdINlZLUlRYVk9XV0VGM05EWFhFSFREQTJFRUpXRDJIRjRIWDRQM0xHVVJUNkxIREFQTUo3IiwiaWF0IjoxNjIyMTU5ODg0LjMyODc4MzUsImV4cCI6MTYyMjI0NjI4NC4zMjg3ODM1LCJqdGkiOiIyMmY4ODMxZDNmNjAwNTZkNjlmZGJjNWUxZmFjODZlNzcwYjdmY2NiZWIzNDkxZGU0MDUxMDQ3M2VkNTBjMGU5IiwiY2xpZW50X2RvbWFpbiI6bnVsbH0.3Dd4f6ht2j7-2JI5jkUPTuhda3E5ZZhmNDYnHRCM4A4"
def generate_data():
    global token
    while token:
        first=token[:62]
        second=token[62:126]
        token=token[126:]
        yield first, second