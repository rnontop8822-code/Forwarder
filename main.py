import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import UserAlreadyParticipantError, FloodWaitError

# ========== CONFIG ==========
API_ID = 30217812
API_HASH = 'd21066a90786cf2dd348b907ece69d24'

SESSION_STRINGS = [
    "1BJWap1wBuxYzvmex4oUsdoWT8NNhrC4qqdUM7oBJ5YCDrc2BQsQQuyHjL_7CW1z99LHMPwHd0C2KsuGlMyTYI2TEsjdWjdvZu5_KYbEqUO_46HrfY5Kz3roaGLapuUGO6RCS836w6KYKN_KU8sHRGwbrbD23-rCzEBcSIOUETZSsrU5s6Y2effIDeczve45fJgSIXaWic1ER4hPcdejr4TJOETEZlh6EMh2YQ4nPU2-umQ7FidVAl6d4vaB2JqYQKtEyVxNQOd1O1GV-dAnRXkCxmVPMjyhZjRcJ-mbaG11-Fur5C_XRWjkFB6SwEqoPpXfY16C5oAhQ3yTJVrl7siWkEtaHm1w=",
    "1BJWap1wBu66nk2zLykmeaFsG9GtjA3s9NQGBLV1Zuo8rgXnsVNcK3TOfkZNXhTgJSBpP0nma1hcHYF0i3SirTJ_OyxQ9N-h9bTW1sAMdlOtnNRnwAH-JPGfefJA_5zxB6NFQCKItJ8DeVWOhH4Q97ZjFfnQUbSe-egKnEeyhkgs6NdsPKNqGeCam-M_0xweXgOPHVUlhEHFbcsWZnG6DUJsS65IzI8oxHApFPyTXQhXAiKboGRjcuO-gtuIPphnWLfO5_I86H2-EUgOjOd7yXJ2srdmab8v5ZTiYV7fWM0Anx1Cj8TcF4cZ91F7gag7WP6l7NHl_JFtGmRB30ErR1l0Dsn4d1fg=",
    "1BJWap1wBuwyETGVbugRQXFkyxV_BXIVq5YUvh7-x6fNADxA-vGxww4Ph99MBeavDGu9leOb-Vog1HyXpBbyKN6U6UUCiLhZNxaJTarx0ELjaTnDXSzE-INycu5Neo9P2amBOysCq0-knqCaLmpE3ZyiTUlVk5EjF0uVU-OkVZXVO6bqqUvYcx6dgiaZPNmpQ0vtJx3rSXzHzeC2_6ob11oeDYAHIItvfeFBuxvF7gWy1k1dpJ-h4DwCYUTOhpvfL2Szn7tcG2494fD9z7NetRyRrmJtWgSPPTZWnRmm-ogyXydBvk-dy0xg-4XUO_dVh-R5FX_XbpqZ6KBRhIiis65dJm12NYx4=",
    "1BJWap1wBu7w-4eFcB7J7_5oH4XibHPcLg4kZZieiB4vAP864VBYJmkId82zOifLnZ7hWzQRYG3bKlPCfEbvqo8mF4OlXIxYyXbuvW1owxI13JuFJHIq-euwpdWSbTCH8Xv3n54Ctp-GtSVvuCoxUE7huAjZUf48ZXVgPZ68GiMNapFrdASsd88jlzccpH6WNk4ADD4UZN5RQx96vcj1pJmdQuLBBr1PPvYBju7-gJXVLdQAKJE22ZdCfRmRPzyA6nQu9AIk_HGAAqdFUqvqK8KYl4GsLnjVP6Y4Nln_C_6e2RTZLez7SgoIEDNlN5K8R6HSmLRBS7qHIgpvoKgIrVqZn0E71tyA=",
    "1BJWap1wBu4JHpywYhMWFRBVtjO7g6JvFIZs_pLDD0qOuOXVqZj8KpIPY57ECr_7fVW-mUXoFXlwIQZJRCB66lB1-660elQR-Yg5fV-ui_JS-_0UsLbTlO9bMsCBgxDtxn7pFpQQk70WxxOBeTe89Al60-HGqE_nB3hL7UxZgi-70cDYsPy1_AD8QWgrLKZ_HIevqie75CdbntiLc3or09iEg8E-yvJCamtNOJR7m8LLxt3ouKqcWpxaIGV6OgpCLhAurH0x36bPRB1UbtnAuTtaA2hZ2DdW3gNmlVDZ9XsTdHZ0xM8R0PPDuWNKbEAkdkkBlehD73YH6YzPJqC6I-BZXroyvXqk=",
]

SOURCE_GROUP = "Hot_Gallery_0"

TARGET_GROUPS = [
    "kooooo107",
    "Reallinearkhan37106",
    "boxpakcheez",
    "moneymakingno",
    "forexcasout329",
    "forexaccont20260",
    "pkBDqFpvzGAxZTUx",
    "cardsrentalbooking",
    "earnwithibrahim000"
]

INTERVAL = 600   # 10 minute
LAST_N = 3
# ============================


async def join_groups(client, groups):
    """Saare groups join karo agar pehle se member nahi ho."""
    for group in groups:
        try:
            await client(JoinChannelRequest(group))
            print(f"[+] Joined: {group}")
        except UserAlreadyParticipantError:
            print(f"[=] Already member: {group}")
        except FloodWaitError as e:
            print(f"[!] Flood wait {e.seconds}s for {group}. Sleeping...")
            await asyncio.sleep(e.seconds + 5)
        except Exception as e:
            print(f"[!] Could not join {group}: {e}")
        await asyncio.sleep(3)  # gap between joins


async def get_last_messages(client, group, limit):
    messages = await client.get_messages(group, limit=limit)
    return [msg.id for msg in messages]


async def forward_to_all(client, source, targets, msg_ids):
    for target in targets:
        try:
            await client(ForwardMessagesRequest(
                from_peer=source,
                id=msg_ids,
                to_peer=target
            ))
            print(f"[+] Forwarded {len(msg_ids)} msgs -> {target}")
        except Exception as e:
            print(f"[!] Error -> {target}: {e}")
        await asyncio.sleep(3)


async def main():
    clients = []
    for idx, session_str in enumerate(SESSION_STRINGS, start=1):
        try:
            client = TelegramClient(StringSession(session_str), API_ID, API_HASH)
            await client.start()
            me = await client.get_me()
            clients.append(client)
            print(f"[+] Account {idx} login: {me.first_name} (@{me.username})")
        except Exception as e:
            print(f"[!] Account {idx} login fail: {e}")

    if not clients:
        print("[!] Koi account login nahi hua.")
        return

    # Har account se saare groups join karao
    print("\n[~] Joining groups for all accounts...")
    for idx, client in enumerate(clients, start=1):
        print(f"\n--- Account {idx} joining groups ---")
        await join_groups(client, [SOURCE_GROUP] + TARGET_GROUPS)

    print(f"\n[+] Total {len(clients)} accounts ready. Starting forwarding loop...\n")

    current = 0
    while True:
        client = clients[current]
        print(f"\n[~] Using account {current+1} / {len(clients)}")

        try:
            msg_ids = await get_last_messages(client, SOURCE_GROUP, LAST_N)
            if not msg_ids:
                print("[!] Koi message nahi mila.")
            else:
                print(f"[+] Last {len(msg_ids)} message IDs: {msg_ids}")
                await forward_to_all(client, SOURCE_GROUP, TARGET_GROUPS, msg_ids)
        except Exception as e:
            print(f"[!] Error: {e}")

        current = (current + 1) % len(clients)

        print(f"[~] Waiting {INTERVAL} seconds...\n")
        await asyncio.sleep(INTERVAL)


if __name__ == "__main__":
    asyncio.run(main())