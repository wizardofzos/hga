# pip install django-battlenet



def getAvatarImgUrl(region, thumbnail):
    return "http://render-api-%s.worldofwarcraft.com/static-render/%s/%s" % (region, region, thumbnail)

