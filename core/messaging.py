from core.supabase_client import supabase
from typing import List, Dict
import threading

class Messaging:
    def __init__(self, current_user_id: str):
        self.current_user_id = current_user_id
        self.message_callback = None

    def send_message(self, receiver_id: str, content: str) -> bool:
        try:
            data = {
                'sender_id': self.current_user_id,
                'receiver_id': receiver_id,
                'content': content
            }
            supabase.table('messages').insert(data).execute()
            return True
        except Exception as e:
            print(f"Error sending message: {e}")
            return False

    def get_chat_history(self, other_user_id: str) -> List[Dict]:
        try:
            response = supabase.table('messages').select('*').or_(
                f"sender_id.eq.{self.current_user_id},receiver_id.eq.{other_user_id}",
                f"sender_id.eq.{other_user_id},receiver_id.eq.{self.current_user_id}"
            ).order('created_at').execute()
            return response.data
        except Exception as e:
            print(f"Error fetching chat history: {e}")
            return []

    def subscribe_to_messages(self, other_user_id: str, callback):
        self.message_callback = callback
        def listen():
            channel = supabase.channel('messages')
            channel.on('postgres_changes', {
                'event': 'INSERT',
                'schema': 'public',
                'table': 'messages',
                'filter': f"or(and(sender_id=eq.{self.current_user_id},receiver_id=eq.{other_user_id}),and(sender_id=eq.{other_user_id},receiver_id=eq.{self.current_user_id}))"
            }, self._on_message)
            channel.subscribe()

        threading.Thread(target=listen, daemon=True).start()

    def _on_message(self, payload):
        if self.message_callback:
            self.message_callback(payload['new'])