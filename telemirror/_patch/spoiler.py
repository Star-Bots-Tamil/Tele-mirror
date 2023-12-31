def patch_input_media_with_spoiler():
    """Patch `utils.get_input_media` to work with spoiler"""
    from telethon import utils

    def patch_input_media_spoiler(fn):
        from functools import wraps

        @wraps(fn)
        def wrapper(
            media,
            *,
            is_photo=False,
            attributes=None,
            force_document=False,
            voice_note=False,
            video_note=False,
            supports_streaming=False,
            ttl=None,
            spoiler=False,
        ):
            input_media = fn(
                media=media,
                is_photo=is_photo,
                attributes=attributes,
                force_document=force_document,
                voice_note=voice_note,
                video_note=video_note,
                supports_streaming=supports_streaming,
                ttl=ttl,
            )
            if hasattr(media, "spoiler"):
                input_media.spoiler = media.spoiler or spoiler
            return input_media

        return wrapper

    utils.get_input_media = patch_input_media_spoiler(utils.get_input_media)
