import urllib.request

url = "https://rr2---sn-2gv8pqxgn5g-u0je.googlevideo.com/videoplayback?expire=1688161703&ei=R_meZIS_BomiobIP-bG_8Aw&ip=45.6.5.101&id=o-AFeOc2G4onCDdoCdcrnHNs8uFsBhRuH-KEoeGgfif0ux&itag=22&source=youtube&requiressl=yes&mh=bj&mm=31%2C29&mn=sn-2gv8pqxgn5g-u0je%2Csn-j5cax8pnpvo-x1xey&ms=au%2Crdu&mv=m&mvi=2&pl=24&initcwndbps=655000&vprv=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=248.012&lmt=1630640758569478&mt=1688139951&fvip=4&fexp=24007246%2C24363391&beids=24350017&c=ANDROID_MUSIC&txp=5532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOIJoTTM-Zie35zjE6zSFRFoVjVTLY-aapG6V20KkgZPAiB8pJEkWZx0Vw9ZfWIVyBoJobpsCxR8VLpcp3Cw08x5Xw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAMJgpkn9OldP4lsozyJZh7pEKKVl3YX1_xsWrF5KsjNUAiEA2ge5YxBEJZTJv7gtuoEVcOQW9KiS21Vm4MLCNTZGlws%3D"
file_name = "video.mp4"

urllib.request.urlretrieve(url, file_name)

print("Video guardado exitosamente como", file_name)
