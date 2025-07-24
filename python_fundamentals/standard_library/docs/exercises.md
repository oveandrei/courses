# A list of exercises for each library in order to strengthen your learning

## File and Filesystem Operations

### OS

**MRP - Minimum Requirements Product:**

Build a CLI tool that lists, renames, or deletes files in a given directory.

**Requirements:**

1. Accept a directory path from the user.
2. Print all file names in that directory.
3. Allow the user to rename or delete a selected file.

**Required usage:**

* `os.listdir()`, `os.rename()`, `os.remove()`, `os.path.exists()`

---

### shutil

**MRP:**

Build a backup script that copies files from a folder to a backup folder.

**Requirements:**

1. Ask the user for source and destination directories.
2. Copy all `.txt` files to the backup directory.
3. Show total disk usage before and after the copy.

**Required usage:**

* `shutil.copy()`, `shutil.disk_usage()`

---

### glob

**MRP:**

Create a script that finds all `.log` files inside a directory.

**Requirements:**

1. Let the user specify a directory.
2. Recursively list all `.log` files using a pattern.
3. Save the list to a file

**Required usage:**

* `glob.glob("**/*.log", recursive=True)`

---

### pathlib

**MRP:**

Build a tool that checks if given file paths exists and whether they're files or folders

**Requirements:**

1. Accept a list of paths from the user
2. For each, check if it exists, and whether it's a file or directory.
3. Print the result nicely formatted.

**Required usage:**

* `Path.exists()`, `Path.is_file()`, `Path.is_dir()`, `Path.iterdir()`

---

### tempfile

**MRP:**

Create a temporary file where the user can write a note.

**Requirements:**

1. Create a temporary file.
2. Let the user write text into it.
3. Print the content and auto-delete it on exit.

**Required usage:**

* `tempfile.NamedTemporaryFile()`

---

## Mathematics and Numbers

### math

**MRP:**

Create a calculator that performs basic mathematical operations and returns constants.

**Requirements:**

1. Accept operation name from user: sqrt, log, sin, ceil.
2. Ask for needed numbers.
3. Return results and show `math.pi`.

**Required usage:**

* `math.sqrt()`, `math.log()`, `math.sin()`, `math.ceil()`, `math.pi`

---

### random

**MRP:**

Build a number guessing game

**Requirements:**

1. Randomly generate a number between 1 and 100.
2. User has 5 tries to guess it.
3. Tell the user if they guessed too high or too low.

**Required usage:**

* `random.randint()`

---

### statistics

**MRP:**

Analyze a list of user-input numbers and print some basic stats.

**Requirements:**

1. User inputs a list of numbers (e.g., 5, 10, 15).
2. Display mean, median, and standard deviation

**Required usage:**

* `statistics.mean()`, `statistics.median()`, `statistics.stdev()`

---

### decimal

**MRP:**

Create a calculator that avoids floatin point errors.

**Requirements:**

1. Accept 2 decimal numbers as input.
2. Add and multiply them precisely.
3. Show output with 3 decimal places.

**Required usage:**

* `decimal.Decimal()`, `decimal.getcontext().prec`

---

### heapq

**MRP:**

Build a task scheduler with task priorities.

**Requirements:**

1. Accept tasks with priorities from the user.
2. Print taks in the correct order of execution.

**Required usage:**

* `heapq.heappush()`, `heapq.heappop()`

---

### bisect

**MRP:**

Maintain a sorted list of numbers as user adds more.

**Requirements:**

1. Start with an empty list.
2. On each new number input, insert in sorted position.
3. Print the sorted list.

**Required usage:**

* `bisect.insort()`, `bisect.bisect_left()`

---

## Data Structures and Algorithms

### array

**MRP:**

Create a memory-efficient number storage tool.

**Requirements:**

1. Accept a list of integers.
2. Store them in an array and print the total size.

**Required usage:**

* `array.array()`

---

### collections

**MRP:**

Analyze word frequency in a paragraph.

**Requirements:**

1. Ask the user to enter a paragraph.
2. Count how often each word appears.

**Required usage:**

* `collections.Counter()`

---

### reprlib

**MRP:**

Show a shortened preview of a long list.

**Requirements:**

1. Generate a list of 1000 elements.
2. Show a safe, short represenation of it.

**Required usage:**

* `reprlib.repr()`

---

### pprint

**MRP:**

Pretty-print neste JSON data.

**Requirements:**

1. Load a sample nested dictionary.
2. Print it clearly formatted.

**Required usage:**

* `pprint.pprint()`

---

### enum

**MRP:**

Create a color picker using Enums

**Requirements:**

1. Define an Enum for colors: RED, GREEN, BLUE.
2. Let user select a color and print its value.

**Required usage:**

* `enum.Enum`

---

### functools

**MRP:**

Cache results of an expensive calculation.

**Requirements:**

1. Simulate a slow function (e.g., `sleep`)
2. Use caching to avoid recalculating.

**Required usage:**

* `functools.lru_cache`

---

### itertools

**MRP:**

Generate all possible pairings from a list of students.

**Requirements:**

1. Accept a list of names.
2. Show all 2-person combinations

**Required usage:**

* `itertools.combinations()`

---

### operator

**MRP:**

Sort a list of people (dicts) by age using `itemgetter`.

**Requirements:**

1. Create a list of dictionaries with `name` and `age`.
2. Sort and display people by age.

**Required usage:**

* `operator.itemgetter()`

---

## Text Processing and String Handling

### re

**MRP:**

Build a regex-based search tool for validating email addresses.

**Requirements:**

1. Ask the user for an email address.
2. Use regex to verify its format.
3. Tell the user if it's valid or not.

**Required usage:**

* `re.match()`
* `re.compile()`

---

### string

**MRP:**

Generate a random password using predefined character sets.

**Requirements:**

1. Combine letters, digits, and punctuation.
2. Randomly generate a password of length 10.
3. Display the password.

**Required usage:**

* `string.ascii_letters`
* `string.digits`
* `string.punctuation`

---

### textwrap

**MRP:**

Format a block of user input text to 40 characters width per line.

**Requirements:**

1. Accept a multi-line input from the user.
2. Wrap each paragraph at 40 characters.
3. Print formatted version.

**Required usage:**

* `textwrap.fill()`

---

### unicodedata

**MRP:**

Display the name and category of each character in a string.

**Requirements:**

1. Accept a string from the user.
2. For each character, print its Unicode name and category.

**Required usage:**

* `unicodedata.name()`
* `unicodedata.category()`

---

### difflib

**MRP:**

Compare two texts and highlight differences line-by-line.

**Requirements:**

1. Accept two strings (multi-line) from the user.
2. Print a diff comparison.

**Required usage:**

* `difflib.ndiff()`
* `difflib.unified_diff()`

---

### stringprep

**MRP:**

Normalize a string for safe network transmission.

**Requirements:**

1. Accept a username.
2. Prepare it using normalization for IDNA.

**Required usage:**

* `stringprep.in_table_a1()` *(or other tables)*

---

### html.parser

**MRP:**

Extract all links from a block of HTML text.

**Requirements:**

1. Input a string of raw HTML.
2. Parse it and print all anchor tags and their `href`.

**Required usage:**

* `html.parser.HTMLParser`

---

## Internet Protocols and Web

### urllib.request

**MRP:**

Download the HTML content of a given website.

**Requirements:**

1. Accept a URL.
2. Fetch and display the first 10 lines of HTML content.

**Required usage:**

* `urllib.request.urlopen()`

---

### smtplib

**MRP:**

Send a test email using a configured SMTP server.

**Requirements:**

1. Ask for sender, recipient, and message body.
2. Send an email through SMTP.

**Required usage:**

* `smtplib.SMTP()`

---

### email

**MRP:**

Create an email message with a subject and body.

**Requirements:**

1. Ask user for subject and body text.
2. Compose a MIME-compliant message.

**Required usage:**

* `email.message.EmailMessage`

---

### json

**MRP:**

Read and write data to a JSON file.

**Requirements:**

1. Ask for user name and age.
2. Save to `data.json`.
3. Load and display the data.

**Required usage:**

* `json.dump()`
* `json.load()`

---

### xmlrpc.client

**MRP:**

Call a public XML-RPC API method.

**Requirements:**

1. Use a test XML-RPC server.
2. Call a method like `add(2, 3)` and print result.

**Required usage:**

* `xmlrpc.client.ServerProxy`

---

### xmlrpc.server

**MRP:**

Create a local XML-RPC server with one exposed function.

**Requirements:**

1. Define a function (e.g., multiply).
2. Register and serve it over localhost.

**Required usage:**

* `xmlrpc.server.SimpleXMLRPCServer`

---

## Dates and Time

### datetime

**MRP:**

Calculate the number of days between two dates.

**Requirements:**

1. Ask the user for two dates.
2. Parse them and calculate the difference in days.

**Required usage:**

* `datetime.strptime()`
* `datetime.date`

---

### timeit

**MRP:**

Compare the speed of list comprehension vs `map()`.

**Requirements:**

1. Define a function that doubles a number.
2. Time both approaches with 10,000 elements.

**Required usage:**

* `timeit.timeit()`

---

## Data Formats and Serialization

### csv

**MRP:**

Read data from a CSV file and print each row.

**Requirements:**

1. Open and read a file `students.csv`.
2. Print name and score of each student.

**Required usage:**

* `csv.reader`

---

### sqlite3

**MRP:**

Create a local database to store tasks.

**Requirements:**

1. Create a `tasks` table.
2. Insert and list tasks.

**Required usage:**

* `sqlite3.connect()`
* `cursor.execute()`

---

### zipfile

**MRP:**

Archive all `.txt` files in a directory.

**Requirements:**

1. Accept a directory path.
2. Create a zip file with all `.txt` files inside.

**Required usage:**

* `zipfile.ZipFile()`

---

### tarfile

**MRP:**

Extract the contents of a `.tar.gz` archive.

**Requirements:**

1. Ask for the archive path.
2. Extract all files to a folder.

**Required usage:**

* `tarfile.open()`

---

### zlib / bz2 / lzma

**MRP:**

Compress and decompress a text message.

**Requirements:**

1. Accept a string from the user.
2. Compress and then decompress it.
3. Verify original = decompressed.

**Required usage:**

* `zlib.compress()`, `zlib.decompress()`
* or `bz2.compress()` / `lzma.compress()`

---

## Security and Cryptography

### hashlib

**MRP:**

Create and compare SHA-256 hashes.

**Requirements:**

1. Ask for two strings.
2. Hash both and compare.

**Required usage:**

* `hashlib.sha256()`

---

### hmac

**MRP:**

Generate an HMAC from a message and key.

**Requirements:**

1. Ask for message and secret key.
2. Generate and print the HMAC.

**Required usage:**

* `hmac.new()`

---

### secrets

**MRP:**

Generate a secure token for password reset.

**Requirements:**

1. Generate a random secure token.
2. Print it.

**Required usage:**

* `secrets.token_urlsafe()`

---

## Utilities and Language Features

### sys

**MRP:**

Display the command-line arguments passed to a Python script.

**Requirements:**

1. Print all arguments passed to the script.
2. Show the name of the script and arguments separately.

**Required usage:**

* `sys.argv`

---

### argparse

**MRP:**

Build a CLI tool that takes user name and age as arguments.

**Requirements:**

1. Accept `--name` and `--age` via CLI.
2. Print a greeting using the inputs.

**Required usage:**

* `argparse.ArgumentParser`

---

### contextlib

**MRP:**

Create a context manager that opens and safely closes a file.

**Requirements:**

1. Use a custom context manager or `contextlib` to open a file.
2. Ensure the file is properly closed after writing.

**Required usage:**

* `contextlib.contextmanager`

---

### abc

**MRP:**

Enforce implementation of a method in subclasses.

**Requirements:**

1. Define an abstract base class `Shape` with a method `area`.
2. Create a `Circle` class that implements it.

**Required usage:**

* `abc.ABC`
* `@abstractmethod`

---

### typing

**MRP:**

Add type hints to a simple calculator function.

**Requirements:**

1. Write a function that adds two numbers.
2. Annotate input and return types.

**Required usage:**

* `typing.Annotated`, `typing.List`, etc.

---

### dataclasses

**MRP:**

Create a data structure to store user information.

**Requirements:**

1. Use a `@dataclass` for `User` with `name` and `email`.
2. Instantiate and print an object.

**Required usage:**

* `@dataclass`

---

### warnings

**MRP:**

Warn the user if their input is below a threshold.

**Requirements:**

1. Accept a number.
2. Issue a warning if the number is below 10.

**Required usage:**

* `warnings.warn()`

---

### importlib

**MRP:**

Dynamically import a module by name.

**Requirements:**

1. Ask the user for a module name (e.g., `math`).
2. Import and print available functions.

**Required usage:**

* `importlib.import_module()`

---

### locale

**MRP:**

Format a number and currency for a specific locale.

**Requirements:**

1. Set locale to `en_US` or `fr_FR`.
2. Format number and currency.

**Required usage:**

* `locale.setlocale()`
* `locale.currency()`

---

### gettext

**MRP:**

Simulate translation using `gettext`.

**Requirements:**

1. Mark a string as translatable.
2. Use `gettext` to fetch translation (mocked).

**Required usage:**

* `gettext.gettext()`

---

### codecs

**MRP:**

Read and write a UTF-16 encoded file.

**Requirements:**

1. Write a string to a file in UTF-16.
2. Read and display it back.

**Required usage:**

* `codecs.open()`

---

## Concurrency and Parallelism

### threading

**MRP:**

Run two functions simultaneously using threads.

**Requirements:**

1. Define two simple functions with sleep.
2. Run them concurrently using threads.

**Required usage:**

* `threading.Thread`

---

### concurrent.futures

**MRP:**

Execute multiple I/O-bound tasks in parallel.

**Requirements:**

1. Define a task function.
2. Use `ThreadPoolExecutor` to run 5 tasks.

**Required usage:**

* `concurrent.futures.ThreadPoolExecutor`

---

### multiprocessing

**MRP:**

Perform parallel computation using separate processes.

**Requirements:**

1. Create a CPU-bound function (e.g., square a number).
2. Use `ProcessPoolExecutor` to execute in parallel.

**Required usage:**

* `concurrent.futures.ProcessPoolExecutor`

---

### asyncio

**MRP:**

Download 3 pages asynchronously and display their lengths.

**Requirements:**

1. Use `aiohttp` or simulate async function.
2. Run tasks concurrently.

**Required usage:**

* `async def`, `await`, `asyncio.run()`

---

### queue

**MRP:**

Simulate a producer-consumer system.

**Requirements:**

1. Producer adds tasks to queue.
2. Consumer processes them.

**Required usage:**

* `queue.Queue`
* `put()`, `get()`

---

## Testing and Debugging

### unittest

**MRP:**

Write unit tests for a simple math function.

**Requirements:**

1. Create a function `add(a, b)`.
2. Write 2 test cases using `unittest`.

**Required usage:**

* `unittest.TestCase`

---

### doctest

**MRP:**

Validate a documented example using `doctest`.

**Requirements:**

1. Add an example in a docstring.
2. Use `doctest` to run it.

**Required usage:**

* `doctest.testmod()`

---

### trace

**MRP:**

Track line-by-line execution of a function.

**Requirements:**

1. Write a simple function with logic.
2. Trace and print each executed line.

**Required usage:**

* `trace.Trace()`

---

### pdb

**MRP:**

Debug a broken function using `pdb`.

**Requirements:**

1. Write a function that throws an error.
2. Step through it interactively.

**Required usage:**

* `pdb.set_trace()`

---

### inspect

**MRP:**

Introspect the signature of a function.

**Requirements:**

1. Define a function with 2 arguments.
2. Print its name, parameters, and docstring.

**Required usage:**

* `inspect.signature()`
* `inspect.getdoc()`

---

### traceback

**MRP:**

Print the stack trace of an error.

**Requirements:**

1. Raise and catch an exception.
2. Print the full traceback.

**Required usage:**

* `traceback.format_exc()`

---

### cProfile / profile / pstats

**MRP:**

Profile a CPU-bound function and analyze results.

**Requirements:**

1. Define a recursive function (like Fibonacci).
2. Use profiler to measure time spent.

**Required usage:**

* `cProfile.run()`
* `pstats.Stats`

---

## Memory and Garbage Collection

### gc

**MRP:**

Manually trigger garbage collection.

**Requirements:**

1. Create and delete a large list.
2. Run garbage collection and print stats.

**Required usage:**

* `gc.collect()`
* `gc.get_stats()`

---

### weakref

**MRP:**

Create a weak reference to a large object.

**Requirements:**

1. Create a class and an instance.
2. Reference it with `weakref` and observe when it’s gone.

**Required usage:**

* `weakref.ref()`

---
