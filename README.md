# Echelon

An Anki 2.1 Addon for Hierarchical Tags, with context aware renaming.

Based off the addon we know and love [Hierarchical Tags by pneff](https://ankiweb.net/shared/info/1089921461), ported to anki 2.1 plus some enhancements

* Clicking on a tag such as `it` will no longer show all cards with tags beginning in `it*`
* Allowing any tag separator - configurable in `Tools>Addons>Config`
* Renaming tags appropriate to the tag hierarchy on right click!

![](images/echelon-rename.png)

For example if we have tags:

| Foo | Foo::Bar | Foo::Baz | Foo::Bar::Baz |

Renaming Foo -> Apple:

| Apple | Apple::Bar | Apple::Baz | Apple::Bar::Baz|

Renaming Foo::Bar -> Banana:

| Foo | Banana | Foo::Baz | Banana::Baz |

#### Issues

At the moment anything in the Side Tree Bar will have `Rename Tag` when right clicked. If you clicked on a deck, this won't rename the deck. If you supplied a valid tag name, any tags with the same name as that deck would be renamed according to your input.

| Deck: Italian | *Right Click Rename Tag* | Renames any tags called Italian |

***

As ever feel free to suggest any features or raise any bugs!