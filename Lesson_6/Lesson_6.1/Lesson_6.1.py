
def parse_log(file):

    if file:
        with open(file,"r",encoding="utf-8") as file:
            for line in file:
                ip = line.split(" - - ")[0]
                rsp_and_pth = line.split('"')[0]
                rsp = rsp_and_pth.split()[0]
                pth = rsp_and_pth.split()[1]
                yield(ip, rsp, pth)

if __name__ == "__main__":
   logs = parse_log("nginx_logs.txt")
   for i in logs:
       print(i)