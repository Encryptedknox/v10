from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hi {} โก

๐ก `I am Telegram most Powerful Url Uploader Bot`

<b>โ๏ธ Press /settings to change my settings</b>

Use help button to know how to use me

๐ฆ <b>Maintained By</b> : [MrAbhi2k3](https://t.me/TeleRoidGroup)
"""
    HELP_TEXT = """
You need Help ?? ๐
   
โต First go to the /settings and change the bot behavior as your choice.

โต Send me the custom thumbnail to save it permanently. (๐๐๐๐๐๐๐๐)

โต Now send me the ytdl or direct link.

โต Select the desired option.

โต Then be relaxed your file will be uploaded soon..

โต Use `/caption` to Set caption as Reply to Media

Maintained By : [MrAbhi2k3](https://t.me/TeleRoidGroup)
 
"""
    ABOUT_TEXT = """
**โป๏ธ My Name** : [Url Uploader Bot](http://t.me/UrlUpxBot)

**๐ Channel** : [TeleRoidGroup](https://t.me/TeleRoidGroup)

**๐ก Support** : [TeleRoidGroup](https://t.me/TeleRoid14)

**โ๏ธ Version** : [4.0 Beta](https://t.me/DonateXRobot)

**๐ Source** : [Click Here](https://github.com/PredatorHackerzZ)

**๐บ Heroku** : [Heroku](https://heroku.com/)

**๐ Language :** [Python 3.10.5](https://www.python.org/)

**๐ต๐ฒ Framework :** [Pyrogram 2.0.30](https://docs.pyrogram.org/)

**๐ฒ Developer :** [MrAbhi2k3](https://t.me/MoviesFlixers_DL)

**๐ฆ Maintained By :** [TeamTeleRoid](https://t.me/SamanthaMoviesBot)

"""


    PROGRESS = """
๐ฐ Speed : {3}/s\n\n
๐ Done : {1}\n\n
๐ฅ Tแดแดแดส sษชแดขแด  : {2}\n\n
โณ Tษชแดแด สแดาแด : {4}\n\n
"""
    ID_TEXT = """
๐ Your Telegram ID ๐ข๐ฌ :- <code>{}</code>
"""

    INFO_TEXT = """

 ๐คน First Name : <b>{}</b>

 ๐ดโโ๏ธ Second Name : <b>{}</b>

 ๐ง๐ปโ๐ Username : <b>@{}</b>

 ๐ Telegram Id : <code>{}</code>

 ๐ Profile Link : <b>{}</b>

 ๐ก Dc : <b>{}</b>

 ๐ Language : <b>{}</b>

 ๐ฒ Status : <b>{}</b>
"""

    PLANS = """๐ Thanks for showing interest in Donation

Donate Me For Keep This Bot Up

You Can Send Any Amount 
of 20โน, 30โน, 50โน, 70โน, 100โน, 200โน ๐
 
๐จ Payment Methods:
 
GooglePay / Paytm / PhonPay / UPI

Donate :- `MrAbhi2k3@apl`
 
More Info Contact: @TeleRoid14

"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('โ๏ธ Settings', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('โ Help', callback_data='help'),
        InlineKeyboardButton('๐ฆ About', callback_data='about')
        ],[
        InlineKeyboardButton('๐ฐ Donate', callback_data='donate'),
        InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐? Home', callback_data='home'),
        InlineKeyboardButton('๐ฆ About', callback_data='about')
        ],[
        InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐? Home', callback_data='home'),
        InlineKeyboardButton('๐ฐ Donate', callback_data='donate')
        ],[
        InlineKeyboardButton('โ Help', callback_data='help'),
        InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐ฐ Donate', callback_data='donate'),
        InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
    )
    DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐ก Home', callback_data='home'),
        InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
    )
    TEXT = "sแดษดแด แดแด แดษดส แดแดsแดแดแด แดสแดแดสษดแดษชส แดแด sแดแด ษชแด"
    IFLONG_FILE_NAME = " Only 64 characters can be named . "
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>No preminum plans available in this bot </b>  /help for Details"
    FORMAT_SELECTION = "Now Select the desired formats"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_FILE = "๐ฅ Downloading  File "
    UPLOAD_FILE = " UploadinG ๐ค \n\n To  transfer.sh "
    ANNO_UPLOAD = " UploadinG๐ค \n\n To  anonfiles.com "
    BAY_UPLOAD = " UploadinG๐ค \n\n To  bayfiles.com "
    GO_FILE_UPLOAD = " ๐คUploadinG๐ค \n\n To  gofile.io "
    DOWNLOAD_START = "Trying to Download โ\n\n๐ฎ๐ธ <i>{} ๐ฎ๐ธ</i>"
    UPLOAD_START = "๐ฎ๐ธ <i>{} ๐ฎ๐ธ</i>\n\n๐ค Uploading Please Wait "
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = " JOIN : https://t.me/TGRobot_List\nFor the List of Telegram Bots"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dแดแดกษดสแดแดแดแดแด ษชษด {} sแดแดแดษดแดs.\n\nTสแดษดแดs Fแดส Usษชษดษข Mแด\n\nUแดสแดแดแดแดแด ษชษด {} sแดแดแดษดแดs"
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/TeleRoid14'>@SpEcHlDe</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Cแดsแดแดแด แด?ษชแดแดแด / าษชสแด แดสแดแดสษดแดษชส sแดแด?แดแด. Tสษชs ษชแดแดษขแด แดกษชสส สแด แดsแดแด ษชษด แดสแด แด?ษชแดแดแด / าษชสแด."
    DEL_ETED_CUSTOM_THUMB_NAIL = "โ Cแดsแดแดแด แดสแดแดสษดแดษชส แดสแดแดสแดแด sแดแดแดแดsาแดสสส"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "โ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Nแด แดแดsแดแดแด แดสแดแดสษดแดษชส าแดแดษดแด"
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    FILE_NOT_FOUND = "Error, File not Found!!"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /ren with custom thumbnail support"
    AFTER_GET_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b>โกLinkโก :</b> <code>{}</code>\n\nJoin : @TeleRoidGroup"
    AFTER_GET_DL_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b>โกLinkโก :</b> <code>{}</code>\n\nValid for <b>14</b> days.\nJoin : @TeleRoidGroup"
    #AFTER_GET_DL_LINK = " {} valid for 30 or more days.\n\n Join : @TeleRoidGroup \n For the list of Telegram bots. "
    AFTER_GET_GOFILE_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n<b>File MD5 Checksum :</b> <code>{}</code>\n\n<b>โกLinkโก :</b> <code>{}</code>\n\n Valid untill 10 days of inactivity\nJoin : @TGRobot_List"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS for screenshot of that specific time."""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "Join : @PHListbot \n For the list of Telegram bots. "
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. โ?๏ธ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/TeleRoid14'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process Free users only 1 request per 4 hrs\n
Upgrade your /plans to Remove Time Gaps and For link Processing"""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me ๐๐....</code>"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    CHECK_LINK = "Analysing <b>โ</b>"

    ADD_CAPTION_HELP = """Select an uploaded file/video or forward me <b>Any Telegram File</b> and just write the text you want to be on the file <b>as a reply to the file</b> and the text you wrote will be attached as the caption! ๐คฉ
    
Ex: <a href='https://telegra.ph/file/198bcda5944f787373122.jpg'>See This!</a> ๐"""
