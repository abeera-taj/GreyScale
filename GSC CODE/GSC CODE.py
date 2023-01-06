import struct

file=open("E:\\demo.txt\\ben.BMP", "rb+"); # put your path of image you want to convert in greyscale
s1=file.read(1);
s2=file.read(1);
s3=file.read(4)
fs=struct.unpack("i", s3)[0]; 
print("s3: ",fs)


print("s1: ",s1)
print("s2: ",s2)

file.seek(18); #width and height starts from here
wid=file.read(4); #width
width=struct.unpack("i", wid)[0];
print("width: ", width)

heg=file.read(4); #height
height=struct.unpack("i", heg)[0];
print("height: ", height);

file.seek(10,0);  #to read rgb colors
off=file.read(4);
osset=struct.unpack("i", off)[0];
print("offset value : ", osset);

file.seek(osset); 
for x in range (0, height): #240
    for y in range (0, width): #320
        print("x:", x);
        print("y:", y)
        r=file.read(1);
        b=file.read(1);
        g=file.read(1);
##        print("r:", r)
##        print("b:", b)
##        print("g:", g)
        
        rb=r[0];
        bb=r[0];
        gb=r[0];
        print("rb: ", rb , "bb: " , bb, "gb: ",gb)
        avg=(rb+bb+gb)//3;
        print("Average value is: ", avg);
        
        grey=(int(avg).to_bytes(1, "little"));
        
        pointer=file.tell();
        print(pointer);
        file.seek(pointer-3);

        file.write(grey);

##pointer=file.tell();
##print(pointer);
##file.seek(pointer-3);
        file.write(grey);

        #pointer=file.tell();
        #print(pointer);
        #file.seek(pointer-3);
        file.write(grey);
file.close();


