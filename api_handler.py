__all__ = ['APIHandler']
import time
import aiohttp
import asyncio


class APIHandler:
    def __init__(self, token, page_id):
        self.page_id = page_id
        self.token = token
        self.rest_time = 1 / 3
        self.request = 'https://api.vk.com/method/{0}?v=5.131&{1}&access_token={2}&lang=0'

    async def get_info(self, st_id: int) -> str:
        """Возвращает имя и фамилию пользователя по его идентфикатору
        :param st_id: идентификатор пользователя
        :type st_id: int
        :rtype: str
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    self.request.format("users.get", f"user_id={st_id}", self.token)) as resp:
                person = await resp.json()
                time.sleep(self.rest_time)
                return f"{person['response'][0]['first_name']} {person['response'][0]['last_name']}"

    async def wall_get(self) -> int:
        """Возвращает идентификатор последнего поста на странице пользователя"""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    self.request.format("wall.get", f"owner_id={self.page_id}&count={1}&filter={'owner'}", self.token)) as resp:
                post_id = await resp.json()
                return post_id['response']['items'][0]['id']

    async def likes_get(self, post_id: int) -> list:
        """Возвращает идентификаторы страниц пользователей, оценивших пост
        :param post_id: идентификатор поста
        :type post_id: int
        :rtype: list
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    self.request.format("likes.getList", f"type={'post'}&owner_id={self.page_id}&item_id={post_id}", self.token)) \
                    as resp:
                result = await resp.json()
                return result['response']['items']

    def get_result(self):
        post_id = asyncio.run(self.wall_get())
        likes_list = asyncio.run(self.likes_get(post_id))
        students = [asyncio.run(self.get_info(e)) for e in likes_list]
        return students
