def isHappy(n):
  # every result number appeared
  record = []
  # number's digits in each calc
  digits = []

  while (True):
    # store digits in n
    digits = []
    while (True):
      digits.append(n%10)
      n //= 10
      if (n == 0):
        # it breaks with n = 0
        break;

    # calc sum
    for i in digits:
      # print(i*i)
      n += i*i

    # happy
    if (n == 1):
      return True

    # unhappy loop detect
    elif (n in record):
      return False

    else:
      record.append(n)
      # print(n, "\n")
      continue
    

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
    print("Results saved to /app/bind_mount/output.txt")