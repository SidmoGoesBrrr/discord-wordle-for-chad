import datetime
import random

import nextcord

popular_words = open("text_files/dict-popular.txt").read().splitlines()
all_words = set(word.strip() for word in open("text_files/dict-sowpods.txt"))

EMOJI_CODES = {
    "green": {
        "a": "<:1f1e6:953182496298762260>",
        "b": "<:1f1e7:953182496009388033>",
        "c": "<:1f1e8:953182496235864064>",
        "d": "<:1f1e9:953182496210714685>",
        "e": "<:1f1ea:953182496240074753>",
        "f": "<:1f1eb:953182496307150939>",
        "g": "<:1f1ec:953182495845785621>",
        "h": "<:1f1ed:953182496181350430>",
        "i": "<:1f1ee:953182496235876412>",
        "j": "<:1f1ef:953182496550445076>",
        "k": "<:1f1f0:953182496256847923>",
        "l": "<:1f1f1:953182496210685972>",
        "m": "<:1f1f2:953182496412008468>",
        "n": "<:1f1f3:953182496261046312>",
        "o": "<:1f1f4:953182498299457546>",
        "p": "<:1f1f5:953182496328122389>",
        "q": "<:1f1f6:953182495854166018>",
        "r": "<:1f1f7:953182496202317844>",
        "s": "<:1f1f8:953182496189739039>",
        "t": "<:1f1f9:953182496122634260>",
        "u": "<:1f1fa:953182496122609684>",
        "v": "<:1f1fb:953182496630112286>",
        "w": "<:1f1fc:953182496126799882>",
        "x": "<:1f1fd:953182496277823519>",
        "y": "<:1f1fe:953182600183300117>",
        "z": "<:1f1ff:953182600233615411>",
    },
    "yellow": {
        "a": "<:1f1e6:953183251613245510>",
        "b": "<:1f1e7:953183251571302430>",
        "c": "<:1f1e8:953183251609059358>",
        "d": "<:1f1e9:953183251529355344>",
        "e": "<:1f1ea:953183251596451850>",
        "f": "<:1f1eb:953183251562917928>",
        "g": "<:1f1ec:953183251734859816>",
        "h": "<:1f1ed:953183251495788544>",
        "i": "<:1f1ee:953183251474837574>",
        "j": "<:1f1ef:953183251483226152>",
        "k": "<:1f1f0:953183251504173086>",
        "l": "<:1f1f1:953183251508396032>",
        "m": "<:1f1f2:953183251558727680>",
        "n": "<:1f1f3:953183251554508800>",
        "o": "<:1f1f4:953183251604836352>",
        "p": "<:1f1f5:953183251722276864>",
        "q": "<:1f1f6:953183251529367612>",
        "r": "<:1f1f7:953183251713916938>",
        "s": "<:1f1f8:953183251499978752>",
        "t": "<:1f1f9:953183251512586310>",
        "u": "<:1f1fa:953183251688718366>",
        "v": "<:1f1fb:953183251533561866>",
        "w": "<:1f1fc:953183251290275883>",
        "x": "<:1f1fd:953183251562913792>",
        "y": "<:1f1fe:953183251550318652>",
        "z": "<:1f1ff:953183251529347142>",
    },
    "gray": {
        "a": "<:1f1e6:953180368503201852>",
        "b": "<:1f1e7:953180368410931330>",
        "c": "<:1f1e8:953180368557703220>",
        "d": "<:1f1e9:953180368662560808>",
        "e": "<:1f1ea:953180368402538516>",
        "f": "<:1f1eb:953180368440262707>",
        "g": "<:1f1ec:953180368419319848>",
        "h": "<:1f1ed:953180368591290378>",
        "i": "<:1f1ee:953180368431902740>",
        "j": "<:1f1ef:953180368507392080>",
        "k": "<:1f1f0:953180368461234186>",
        "l": "<:1f1f1:953180368402513941>",
        "m": "<:1f1f2:953180368515768330>",
        "n": "<:1f1f3:953180368327045140>",
        "o": "<:1f1f4:953180368347992064>",
        "p": "<:1f1f5:953180368519970816>",
        "q": "<:1f1f6:953180368360570910>",
        "r": "<:1f1f7:953180368385744976>",
        "s": "<:1f1f8:953180368096342028>",
        "t": "<:1f1f9:953180368515760128>",
        "u": "<:1f1fa:953180368691949578>",
        "v": "<:1f1fb:953180368389963816>",
        "w": "<:1f1fc:953180368452878338>",
        "x": "<:1f1fd:953180368415117332>",
        "y": "<:1f1fe:953180368444477480>",
        "z": "<:1f1ff:953180368536752158>",
    },
}


def generate_colored_word(guess: str, answer: str) -> str:
    """
    Builds a string of emoji codes where each letter is
    colored based on the key:
    - Same letter, same place: Green
    - Same letter, different place: Yellow
    - Different letter: Gray

    Args:
        word (str): The word to be colored
        answer (str): The answer to the word

    Returns:
        str: A string of emoji codes
    """
    colored_word = [EMOJI_CODES["gray"][letter] for letter in guess]
    guess_letters = list(guess)
    answer_letters = list(answer)
    # change colors to green if same letter and same place
    for i in range(len(guess_letters)):
        if guess_letters[i] == answer_letters[i]:
            colored_word[i] = EMOJI_CODES["green"][guess_letters[i]]
            answer_letters[i] = None
            guess_letters[i] = None
    # change colors to yellow if same letter and not the same place
    for i in range(len(guess_letters)):
        if guess_letters[i] is not None and guess_letters[i] in answer_letters:
            colored_word[i] = EMOJI_CODES["yellow"][guess_letters[i]]
            answer_letters[answer_letters.index(guess_letters[i])] = None
    return "".join(colored_word)


def generate_blanks() -> str:
    """
    Generate a string of 5 blank white square emoji characters

    Returns:
        str: A string of white square emojis
    """
    return "\N{WHITE MEDIUM SQUARE}" * 5


def generate_puzzle_embed(user: nextcord.User, puzzle_id: int) -> nextcord.Embed:
    """
    Generate an embed for a new puzzle given the puzzle id and user

    Args:
        user (nextcord.User): The user who submitted the puzzle
        puzzle_id (int): The puzzle ID

    Returns:
        nextcord.Embed: The embed to be sent
    """
    embed = nextcord.Embed(title="Wordle")
    embed.description = "\n".join([generate_blanks()] * 6)
    embed.set_author(name=user.name, icon_url=user.display_avatar.url)
    embed.set_footer(
        text=f"ID: {puzzle_id} ︱ To play, use the command /play!\n"
        "To guess, reply to this message with a word."
    )
    return embed


def update_embed(embed: nextcord.Embed, guess: str) -> nextcord.Embed:
    """
    Updates the embed with the new guesses

    Args:
        embed (nextcord.Embed): The embed to be updated
        puzzle_id (int): The puzzle ID
        guess (str): The guess made by the user

    Returns:
        nextcord.Embed: The updated embed
    """
    puzzle_id = int(embed.footer.text.split()[1])
    answer = popular_words[puzzle_id]
    colored_word = generate_colored_word(guess, answer)
    empty_slot = generate_blanks()
    # replace the first blank with the colored word
    embed.description = embed.description.replace(empty_slot, colored_word, 1)
    # check for game over
    num_empty_slots = embed.description.count(empty_slot)
    if guess == answer:
        if num_empty_slots == 0:
            embed.description += "\n\nPhew!"
        if num_empty_slots == 1:
            embed.description += "\n\nGreat!"
        if num_empty_slots == 2:
            embed.description += "\n\nSplendid!"
        if num_empty_slots == 3:
            embed.description += "\n\nImpressive!"
        if num_empty_slots == 4:
            embed.description += "\n\nMagnificent!"
        if num_empty_slots == 5:
            embed.description += "\n\nGenius!"
    elif num_empty_slots == 0:
        embed.description += f"\n\nThe answer was {answer}!"
    return embed


def is_valid_word(word: str) -> bool:
    """
    Validates a word

    Args:
        word (str): The word to validate

    Returns:
        bool: Whether the word is valid
    """
    return word in all_words


def random_puzzle_id() -> int:
    """
    Generates a random puzzle ID

    Returns:
        int: A random puzzle ID
    """
    return random.randint(0, len(popular_words) - 1)


def daily_puzzle_id() -> int:
    """
    Calculates the puzzle ID for the daily puzzle

    Returns:
        int: The puzzle ID for the daily puzzle
    """
    # calculate days since 1/1/2022 and mod by the number of puzzles
    num_words = len(popular_words)
    time_diff = datetime.datetime.now().date() - datetime.date(2022, 1, 1)
    return time_diff.days % num_words


def is_game_over(embed: nextcord.Embed) -> bool:
    """
    Checks if the game is over in the embed

    Args:
        embed (nextcord.Embed): The embed to check

    Returns:
        bool: Whether the game is over
    """
    return "\n\n" in embed.description





async def process_message_as_guess(
    bot: nextcord.Client, message: nextcord.Message
) -> bool:
    """
    Check if a new message is a reply to a Wordle game.
    If so, validate the guess and update the bot's message.

    Args:
        bot (nextcord.Client): The bot
        message (nextcord.Message): The new message to process

    Returns:
        bool: True if the message was processed as a guess, False otherwise
    """
    # get the message replied to
    ref = message.reference
    if not ref or not isinstance(ref.resolved, nextcord.Message):
        return False
    parent = ref.resolved

    # if the parent message is not the bot's message, ignore it
    if parent.author.id != bot.user.id:
        return False

    # check that the message has embeds
    if not parent.embeds:
        return False

    embed = parent.embeds[0]

    guess = message.content.lower()

    # check that the user is the one playing
    if (
        embed.author.name != message.author.name
        or embed.author.icon_url != message.author.display_avatar.url
    ):
        reply = "Start a new game with /play"
        if embed.author:
            reply = f"This game was started by {embed.author.name}. " + reply
        await message.reply(reply, delete_after=5)
        try:
            await message.delete(delay=5)
        except Exception:
            pass
        return True

    # check that the game is not over
    if is_game_over(embed):
        await message.reply(
            "The game is already over. Start a new game with /play", delete_after=5
        )
        try:
            await message.delete(delay=5)
        except Exception:
            pass
        return True

    # check that a single word is in the message
    if len(message.content.split()) > 1:
        await message.reply(
            "Please respond with a single 5-letter word.", delete_after=5
        )
        try:
            await message.delete(delay=5)
        except Exception:
            pass
        return True

    # check that the word is valid
    if not is_valid_word(guess):
        await message.reply("That is not a valid word", delete_after=5)
        try:
            await message.delete(delay=5)
        except Exception:
            pass
        return True

    # update the embed
    embed = update_embed(embed, guess)
    await parent.edit(embed=embed)

    # attempt to delete the message
    try:
        await message.delete()
    except Exception:
        pass

    return True