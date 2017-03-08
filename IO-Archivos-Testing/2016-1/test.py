def file_to_bytes(path):

    with open(path, 'rb') as file:
        return file.read()


def to_int(databyte):
    size = len(databyte)
    return sum(databyte[i] << (i*8) for i in range(size))


def reverse(data):
    lista = []
    for i in range(len(data)):
        lista.append(data[len(data)-1-i])
    return lista


class WAVMdata:

    @staticmethod
    def get_metadata(header):
        mdata = dict()
        mdata["riff"] = header[:4]
        mdata["size"] = to_int(header[4:8]) + 8
        mdata["wave"] = header[8:12]
        mdata["fmt"] = header[12:16]
        mdata["16"] = to_int(header[16:20])
        mdata["type"] = to_int(header[20:22])
        mdata["nch"] = to_int(header[22:24])
        mdata["fs"] = to_int(header[24:28])
        mdata["bps"] = to_int(header[34:36])
        mdata["init"] = header[36:40]
        mdata["datalen"] = to_int(header[40:44])

        print(mdata)

        if to_int(header[28:32]) != mdata["fs"] * mdata["bps"] * mdata["nch"] / 8\
                or to_int(header[32:34]) != mdata["bps"] * mdata["nch"] / 8\
                or mdata["datalen"] != mdata["size"] - 44:
            print("Houston, tenemos un problema")

    @staticmethod
    def write_mdata(mdata, file):


        file.write(mdata["riff"])
        file.write((mdata["size"] - 8).to_bytes(4, byteorder='little'))
        file.write(mdata["wave"])
        file.write(mdata["fmt"])
        file.write(mdata["16"].to_bytes(4, byteorder='little'))
        file.write(mdata["type"].to_bytes(2, byteorder='little'))
        file.write(mdata["nch"].to_bytes(2, byteorder='little'))
        file.write(mdata["fs"].to_bytes(4, byteorder='little'))
        file.write(int(mdata["fs"] * mdata["bps"] * mdata["nch"] / 8).to_bytes(
            4, byteorder='little'
        ))
        file.write(int(mdata["bps"] * mdata["nch"] / 8).to_bytes(
            2, byteorder='little'
        ))
        file.write(mdata["bps"].to_bytes(2, byteorder='little'))
        file.write(mdata["init"])
        file.write((mdata["datalen"]).to_bytes(4, byteorder='little'))

if __name__ == '__main__':
    path = 'TOP SECRET.iic2233'
    file_read = file_to_bytes(path)
    int = to_int(file_read)
    num = 44
    header = file_read[:num]
    bits_wav = [74300]*4
    bits_gif = [114587, 452976, 54325, 163936]
    wav = []
    gif = []
    for i in range(8):
        if i % 2 == 0:
            wav.append(file_read[num:num+bits_wav[i//2]])
            num = num + bits_wav[i//2]
        elif i % 2 != 0:
            gif.append(file_read[num:num+bits_gif[(i-1)//2]])
            num = num + bits_gif[(i-1)//2]

    new_wav = []
    for i in range(len(wav)):
        new_wav.append(reverse(wav[i]))
    new_wav.reverse()
    print(new_wav)
    print(file_read[44:44+74300], file_read[44+74300+])
    print(wav)
    print(gif)

