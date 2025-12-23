from app.Config.Config import setting
import cloudinary.uploader

cloudinary.config(
    cloud_name = setting.CLOUDINARY_NAME,
    api_key = setting.CLOUDINARY_KEY,
    api_secret = setting.CLOUDINARY_SECRET
)

async def uploadImage(image) -> dict:
    result = cloudinary.uploader.upload(image)
    return {
        "url": result["url"],
        "public_id": result["public_id"]
    }