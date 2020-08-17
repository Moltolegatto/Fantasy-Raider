from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter.constants import BOTH
from PIL import ImageTk, Image
import json
import os
import requests

root = Tk()
root.title("Fantasy Raider Host")
root.geometry("1035x620")
root.iconbitmap('imgs/fr_icon.ico')

#Edit button for changing players within a team
def edit():
    top = Toplevel()
    top.title("Edit Team")
    top.geometry("300x200")
    top.iconbitmap('imgs/fr_icon.ico')

    lable_wteam = Label(top, text="Which team to edit?")
    lable_wteam.grid(row=0, column=0)
    team_en = Entry(top, width=5)
    team_en.grid(row=1, column=0)

    lable_rem = Label(top, text="Name to remove")
    lable_rem.grid(row=2, column=0)
    rem_en = Entry(top, width=30)
    rem_en.grid(row=3, column=0, padx=10)

    lable_ad = Label(top, text="Name to add")
    lable_ad.grid(row=4, column=0)
    ad_en = Entry(top, width=30)
    ad_en.grid(row=5, column=0)

    #Commits the changes made from the edit function
    def change():
        remove_p = rem_en.get()
        add_p = ad_en.get()
        ed_team = int(team_en.get())

        label_rem = Label(top, text=remove_p)
        label_rem.grid(row=7, column=0)

        label_ad = Label(top, text=add_p)
        label_ad.grid(row=8, column=0)

        directory = os.path.dirname(__file__)
        filename = os.path.join(directory, "player_roster.json")

        with open(filename, 'r', encoding="utf-8") as fin:
            temp_roster = json.load(fin)
        temp_roster_new = [add_p if x == remove_p else x for x in temp_roster[ed_team - 1]]
        temp_roster[ed_team - 1] = temp_roster_new

        with open(filename, 'w', encoding="utf-8") as fout:
            json.dump(temp_roster, fout)
        top.destroy()

    confirm_button = Button(top, text="Commit", command=change)
    confirm_button.grid(row=6, column=0, pady=10)

#Adds a new team to the "player roster" json
def add_team():
    top1 = Toplevel()
    top1.title("Add a Team")
    top1.geometry("300x300")
    top1.iconbitmap('imgs/fr_icon.ico')

    label_p1 = Label(top1, text="Raider 1")
    label_p1.grid(row=0, column=0, sticky="N")
    p1_en = Entry(top1, width=30)
    p1_en.grid(row=1, column=0, padx=10)

    label_p2 = Label(top1, text="Raider 2")
    label_p2.grid(row=2, column=0)
    p2_en = Entry(top1, width=30)
    p2_en.grid(row=3, column=0)

    label_p3 = Label(top1, text="Raider 3")
    label_p3.grid(row=4, column=0)
    p3_en = Entry(top1, width=30)
    p3_en.grid(row=5, column=0)

    label_p4 = Label(top1, text="Raider 4")
    label_p4.grid(row=6, column=0)
    p4_en = Entry(top1, width=30)
    p4_en.grid(row=7, column=0)

    label_p5 = Label(top1, text="Raider 5")
    label_p5.grid(row=8, column=0)
    p5_en = Entry(top1, width=30)
    p5_en.grid(row=9, column=0)

    #Commits the changes made with the add function
    def add():
        p1 = p1_en.get()
        p2 = p2_en.get()
        p3 = p3_en.get()
        p4 = p4_en.get()
        p5 = p5_en.get()

        tempteam = []
        tempteam.append(p1)
        tempteam.append(p2)
        tempteam.append(p3)
        tempteam.append(p4)
        tempteam.append(p5)

        with open("player_roster.json", 'r', encoding="utf-8") as fina:
            old = json.load(fina)
        old.append(tempteam)

        with open("player_roster.json", 'w', encoding="utf-8") as fouta:
            json.dump(old, fouta)
        top1.destroy()

    button_add = Button(top1, text="Add team", command=add)
    button_add.grid(row=10, column=0, pady=20)

#Removes a team from the "player roster" json
def remove_team():
    top2 = Toplevel()
    top2.title("Remove Team")
    top2.geometry("220x110")
    top2.iconbitmap('imgs/fr_icon.ico')

    team_rem_label = Label(top2, text="Which number team to remove?")
    team_rem_label.grid(row=0, column=0)

    team_rem_en = Entry(top2, width="5")
    team_rem_en.grid(row=1, column=0)


    #Commits the changes made from the remove_team function
    def remove():
        team_nun = int(team_rem_en.get()) - 1
        with open("player_roster.json", 'r', encoding="utf-8") as finr:
            remove_team = json.load(finr)

        del remove_team[team_nun]

        with open("player_roster.json", 'w', encoding="utf-8") as foutr:
            json.dump(remove_team, foutr)
        top2.destroy()

    remove_button = Button(top2, text="Remove", command=remove)
    remove_button.grid(row=2, column=0, pady=10)


img_frame = Frame(root)
img_frame.grid(row=0, rowspan=4, column=3, columnspan=4, sticky="w", padx=200)

#Creates a frame to display the roster gotten from "player roster" json
roster_frame = Frame(root)
roster_frame.grid(row=0, column=0, sticky="n", columnspan=3)
label_text = "Your Teams"
roster_label = Label(roster_frame, text=label_text)
roster_label.pack()

with open("player_roster.json", 'r', encoding="utf-8") as fin:
    roster = json.load(fin)

roster_text = scrolledtext.ScrolledText(roster_frame, undo=True, height=20, width=80, bg="Grey")
roster_text.pack(expand=False, fill=BOTH)

for r in range(len(roster)):
    team = list(roster[r])
    roster_text.insert(INSERT, f"{r + 1}: {team}\n")
roster_text.configure(state="disabled")

# Refreshes the roster frame with any changes made with edit/add/remove functions
def refresh():
    with open("player_roster.json", 'r', encoding="utf-8") as fin:
        roster = json.load(fin)

    roster_text.configure(state="normal")
    roster_text.delete("1.0", "end")
    for r in range(len(roster)):
        team = list(roster[r])
        roster_text.insert(INSERT, f"{r + 1}: {team}\n")
    roster_text.configure(state="disabled")

# Gets the logs from Warcraftlogs for the player roster
def parse():
    top3 = Toplevel()
    top3.title("Parse Results")
    top3.geometry("1100x300")

    parse_text = scrolledtext.ScrolledText(top3, undo=True, height=20, width=80, bg="black", fg="White", state="normal")
    parse_text.pack(expand=False, fill=BOTH)
    parse_text.tag_config("red", foreground="RED")
    parse_text.tag_config("white", foreground="White")

    # Gets the parse perameters from the main window
    server = server_en.get()
    raid = rid.get()
    region = reg.get()

    avg_tot = []

    
    with open("player_roster.json", 'r', encoding="utf-8") as finp:
        roster_parse = json.load(finp)


    #Cycles through each team in the "player roster" json  
    for i in range(len(roster_parse)):
        #Cycles through each player in a team
        for n in roster_parse[i]:
            url = "https://classic.warcraftlogs.com:443/v1/parses/character/" + n + \
                  "/" + server + "/" + region + "?zone=" + raid + "metric=dps&compare=0&api_key=6796996434cf246743f73accbf1c85ce"
            #Creates the api url and fetches the api data, saving it to a json
            url_obj = requests.get(url)
            parse_data = url_obj.json()
            percent_per_char = []
            encount_prev = None

            #Checks if there is a valid log for given raid and character, if not then checks for p5 no world buffs logs
            if len(parse_data) == 0:
                url = "https://classic.warcraftlogs.com:443/v1/parses/character/" + n + \
                      "/" + server + "/" + region + "?zone=" + raid + "metric=dps&compare=0&partition=4&api_key=6796996434cf246743f73accbf1c85ce"
                url_obj = requests.get(url)
                parse_data = url_obj.json()
                #If no p5 no world buff logs, then returns a message informing user
                if len(parse_data) == 0:
                    parse_text.insert(INSERT, "Invalid character name or character has no recent parses for this raid")
                    break
            #Checks for duplicate boss entries and takes only the highest percentile parse data        
            for x in range(len(parse_data)):
                encount_cur = json.dumps(parse_data[x]['encounterName'])
                if encount_prev == encount_cur:
                    parse_data_cur = json.dumps(parse_data[x]['percentile'])
                    parse_data_prev = json.dumps(parse_data[x - 1]['percentile'])
                    encount_prev = encount_cur
                    if parse_data_cur >= parse_data_prev:
                        percent_per_char[len(percent_per_char) - 1] = float(parse_data_cur)
                    else:
                        continue
                else:
                    parse_data_cur = json.dumps(parse_data[x]['percentile'])
                    percent_per_char.append(float(parse_data_cur))
                    encount_prev = encount_cur

            #Creates a score based on averages of parse data        
            total = sum(percent_per_char)
            aver_len = len(percent_per_char)
            aver = total / aver_len
            avg_tot.append(aver)
            parse_text.configure(state="normal")
            parse_text.insert(INSERT, f"{n}'s average is : {aver}\n")
        parse_text.configure(state="normal")
        parse_text.insert(INSERT, " \n")

        team_tot = int(sum(avg_tot))
        team_tot_av = team_tot / 5

        parse_text.configure(state="normal")
        parse_text.insert(INSERT, f"Team {i + 1}'s total points this week are {team_tot_av}\n", "red")

        parse_text.insert(INSERT, "================================================\n", "white")
        parse_text.configure(state="disabled")

        avg_tot.clear()

#Button positioning
button_frame = Frame(roster_frame)
button_frame.pack(anchor="e")

button_refresh = Button(button_frame, text="Refresh Roster", command=refresh, width=13)
button_refresh.grid(row=0, column=0, pady=10, sticky="w")

button_edit = Button(button_frame, text="Edit", command=edit, width=10)
button_edit.grid(row=0, column=1, padx=10, pady=10, sticky="e")

button_addteam = Button(button_frame, text="Add Team", command=add_team, width=10)
button_addteam.grid(row=0, column=2, sticky="e")

button_removeteam = Button(button_frame, text="Remove Team", command=remove_team, width=12)
button_removeteam.grid(row=0, column=3, padx=10, sticky="e")

options_frame = Frame(root, relief=SUNKEN, borderwidth=1)
options_frame.grid(row=1, column=0, sticky="sw", pady=30, )

parse_label = Label(root, text="Parse can take a while, its not frozen")
parse_label.grid(row=1, column=1, sticky="w", padx=10)

parse_button = Button(root, text="Parse", width=15, height=10, bg="Green", font="Courier", command=parse)
parse_button.grid(row=1, column=2, sticky="w")

raid_label = Label(options_frame, text="Select Raid\n")
raid_label.grid(row=0, column=0, )

rid = StringVar()
rid.set("1002")

reg = StringVar()
reg.set("US")
Radiobutton(options_frame, text="Molten Core", variable=rid, value=1000).grid(row=1, column=0, sticky="w")
Radiobutton(options_frame, text="Onyxia", variable=rid, value=1001).grid(row=2, column=0, sticky="w")
Radiobutton(options_frame, text="Blackwing Lair", variable=rid, value=1002).grid(row=3, column=0, sticky="w")
Radiobutton(options_frame, text="Zuul'Gurub", variable=rid, value=1003).grid(row=4, column=0, sticky="w")
Radiobutton(options_frame, text="AQ20", variable=rid, value=1004).grid(row=5, column=0, sticky="w")
Radiobutton(options_frame, text="AQ40", variable=rid, value=1005).grid(row=6, column=0, sticky="w")

Radiobutton(options_frame, text="US", variable=reg, value="US").grid(row=3, column=1)
Radiobutton(options_frame, text="EU", variable=reg, value="EU").grid(row=4, column=1)

server_label = Label(options_frame, text="Server:")
server_label.grid(row=1, column=1)

server_en = Entry(options_frame)
server_en.grid(row=2, column=1, padx=40)
server_en.insert(0, "Atiesh")

logo_img = ImageTk.PhotoImage(Image.open("imgs/Logo.png"))

logo_label = Label(img_frame, image=logo_img)
logo_label.grid(row=0, column=0, stick="w")

root.mainloop()
