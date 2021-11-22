denominations = [ 1, 2, 5 ]
price = 20
max_count = []
ans_count = 0

for index in range ( 0 , len ( denominations ) ) :
    t = price / denominations [ index ]
    temp = int ( t ) + 1
    max_count.append ( temp )
    print ( temp )

for index0 in range ( 0 , max_count[0] ) :
    for index1 in range ( 0 , max_count[1] ) :
        for index2 in range ( 0 , max_count[2] ) :
            ans0 = index0 * denominations[0]
            ans1 = index1 * denominations[1]
            ans2 = index2 * denominations[2]
            if ans0+ans1+ans2 == price :
                print (".......")
                print ( ans0 , "=", index0 ,"*", denominations[0] )
                print ( ans1 , "=", index1 ,"*", denominations[1] )
                print ( ans2 , "=", index2 ,"*", denominations[2] )
                print ( "=====" , price )
                ans_count += 1
                
print ( ans_count )