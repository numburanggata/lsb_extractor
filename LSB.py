import numpy as np
from PIL import Image
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt

def save_image(npdata, outfilename):
    #plt.imshow(npdata) 
    #plt.savefig(outfilename)
    #im = Image.fromarray(npdata)
    #print(outfilename)
    #im.save(r"D:\\Python\\Naga\\" + outfilename + ".png")
    outimg = Image.fromarray(np.uint8(npdata), "L")
    outimg.show()

#def teken(plane):
    

def shikat(channelori, channelste):
    tekenedo = np.squeeze(channelori, 2)
    tekeneds = np.squeeze(channelste, 2)
    #print(tekened)
    solu = int(256)
    bahanand = np.full((solu, solu), 1)
    
    bitmo = tekenedo & bahanand
    bitms = tekeneds & bahanand
    #print(bitmo)
    #print(bitms)

    simg1, simg2 = [],[]
    for x in range(solu):
        for y in range(solu):
            if y%2 == 0:
                simg1.append(bitms[x,y])
            else:
                simg2.append(bitms[x,y])
    #print(bitms)
    #print(simg1)
    #print(simg2)

    skey1, skey2 = [],[]
    for x in range(solu):
        for y in range(solu):
            if y%2 == 0:
                skey1.append(bitmo[x,y])
            else:
                skey2.append(bitmo[x,y])
    #print(bitmo)
    #print(skey1)
    #print(skey2)
    #skey1
    #skey2

    msg1 = np.bitwise_xor(simg1, skey1)
    msg2 = np.bitwise_xor(simg2, skey2)

    res = []
    i,l = 0,0
    for x in range(solu*solu):
        if x%2 == 0:
            res.append(msg2[i])
            i+=1
        else:
            res.append(msg1[l])
            l+=1
    print(len(res))
        
    #res = bitmo ^ bitms
    
    #print(res)
    maxed = [i * 255 for i in res]
    #tex = ''
    #for i in range(256):
    #    tex = tex
    #print(res[0])
    #x = res[0]
    #x = np.array2string(res[0], separator=',', suppress_small=True)
    #print(x)
    #n = int('0b110100001100101011011000110110001101111', 2)
    sun = ''
    
    #for h in range(7):
    #    for i in range(solu):
    #        for l in range(int(solu/8)):
    #            n = chr(int('0b' + "".join(map(str, res[i, h+(l*8):h+((l+1)*8)])), 2))
    #            sun += n
    for x in range(int(solu*solu/8)):
        n = chr(int('0b' + "".join(map(str, res[(x*8):(x+1)*8])), 2))
        sun += n
    print(sun)
    textfile = open('textfile.txt', 'w', encoding="utf-8")
    textfile.write(sun)
    textfile.close()
            #print(n)
        #print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
    #    
    #        print(res[i,l*8:((l+1)*8)])
        
    #print(maxed)
    return np.reshape(maxed, (-1,256))
    
    #channel

img = Image.open(r'D:\Python\Naga\d1.jpg')
stego = Image.open(r'D:\Python\Naga\d2.jpg')

#print(img.format)
#print(img.size)
#print(stego.size)
#print(img.mode)

#img.load()
dataori = np.asarray(img)
dataste = np.asarray(stego)
#print(data)

[Bori,Gori,Rori] = np.dsplit(dataori, dataori.shape[-1])
[Bste,Gste,Rste] = np.dsplit(dataste, dataste.shape[-1])
#print(B.shape)
#print(B)

#np.full((450, 800), 254)
#Br = np.append(B, np.atleast_3d(np.zeros((450,800,2))),2)
#print(Br.shape)
#print(Br)
#save_image(Br, "batu.tiff")



#save_image(np.bitwise_and(np.bitwise_and(shikat(Bori, Bste), shikat(Gori, Gste)), shikat(Rori, Rste)), "Br.png")
#save_image(shikat(Bori, Bste), "Br")
#save_image(shikat(Gori, Gste), "Gr")
save_image(shikat(Rori, Rste), "Rr")
