def reclusive(cnt):
   
    if cnt==101:
        return
    print(str(cnt+1),"번째 실행")
    reclusive(cnt+1)
    print(str(cnt),"번째 종료")
    

reclusive(1)