def validateIP(ip):
  array = ip.split('.')
  if len(array) == 4:
    for x in array:
      if x == "" or not x.isdigit():
        return False
      if int(x) < 0 or int(x) > 255:
        return False
    return True
  return False

ip = '192.168.0.oops'
print validateIP(ip)

ip = '0.0.0.0'
print validateIP(ip)

ip = '123.24.59.99'
print validateIP(ip)

ip = '192.168.123.456'
print validateIP(ip)