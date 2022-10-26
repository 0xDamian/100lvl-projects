
# converts seconds to minutes

# y'all don't want me to explain this thing tbh lmao
# but yeah, code works just fine
def convert(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%02d:%02d" % (minutes, seconds)
      
n = int(input("Input Time in Seconds: "))
print(convert(n))