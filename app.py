import subprocess
 
accesstoken = "token"#<이전단계에서 받은 accesstoken을 사용>
bandkey = "bandkey"#<이전단계에서 받은 밴드key 사용>
Content = "contents"#<올리고 싶은 밴드 내용 본문>
 
sendBandPost = 'curl -d "access_token='+accesstoken+'&band_key='+bandkey+'&content='+Content+'" http://openapi.band.us/v2.2/band/post/create'
subprocess.call(sendBandPost, shell=True)