# Access Items

# List items are indexed and you can access them by referring to the index number.

#Example:

# The website internally keeps users in a list:

# User 1 → First registered user

# User 2 → Second registered user

# User 3 → Third registered user

# …

# When the admin clicks on “View User 3”, the system directly opens the 3rd user’s profile.
# This is accessing an item by index in a list



# Negative Indexing

# Negative indexing means start from the end

# -1 refers to the last item, -2 refers to the second last item etc.

#Example:

# Now imagine a chat application like WhatsApp or Slack.

# Messages are stored in a list:

# The newest message is at the end.

# If you want:

# The latest message → you take the last item

# The second latest message → second last item

# That is negative indexing.





# Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.

#Example
# Now think about pagination in websites.

# A blog website has 100 articles, but it shows:

# Only 10 articles per page

# Page 1 shows:

# Articles 1 to 10

# Page 2 shows:

# Articles 11 to 20

# The backend takes a range from the list of all articles and sends only that part to the frontend.

# That is Range of Indexes.