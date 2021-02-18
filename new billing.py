from tkinter import *
import math, random, os
from tkinter import messagebox
class bill_app:
    def __init__ (self, root):
        self.root = root
        self.root.title("LA BENNETT PIZZA")
        self.root.geometry("1920x1080+0+0")
        title = Label(self.root, text = "WELCOME TO LA BENNETT PIZZA",bd=12, relief=GROOVE, bg="black", fg="yellow", font=("times new roman",30,"bold"), pady=2).pack(fill=X)


        self.farmhouse_ = IntVar()
        self.margherita_ = IntVar()
        self.capsicum_ = IntVar()
        self.pepperoni_ = IntVar()
        self.brooklyn_ = IntVar()
        self.chargrilled_ = IntVar()
        self.paneertikka_ = IntVar()
        self.mexican_ = IntVar()
        self.pepper5_ = IntVar()
        self.prawn_ = IntVar()

        self.garlic_bread_ = IntVar()
        self.veg_wraps_ = IntVar()
        self.non_veg_wraps_ = IntVar()
        self.chicken_wings_ = IntVar()
        self.veg_tacos_ = IntVar()
        self.non_tacos_ = IntVar()
        self.veg_burrito_ = IntVar()
        self.non_veg_burrito_ = IntVar()
        self.cheese_sticks_ = IntVar()
        self.fishnchips_ = IntVar()

        self.chocolava_ = IntVar()
        self.cheesecake_ = IntVar()
        self.brownie_ = IntVar()
        self.sundae_ = IntVar()
        self.choco_fudge_ = IntVar()
        self.tiramisu_ = IntVar()
        self.pudding_ = IntVar()
        self.waffles_ = IntVar()
        self.pancakes_ = IntVar()
        self.carrot_cake_ = IntVar()

        self.pepsi_ = IntVar()
        self.coca_cola_ = IntVar()
        self.fanta_ = IntVar()
        self.fruit_juice_ = IntVar()
        self.sprite_ = IntVar()
        self.limca_ = IntVar()
        self.fruit_beer_ = IntVar()
        self.frooti_ = IntVar()
        self.slice_1 = IntVar()
        self.banta_ = IntVar()

        self.pizzas_price = StringVar()
        self.sides_price = StringVar()
        self.desserts_price = StringVar()
        self.beverages_price = StringVar()

        self.pizzas_tax = StringVar()
        self.sides_tax = StringVar()
        self.desserts_tax = StringVar()
        self.beverages_tax = StringVar()

        self.c_name = StringVar()
        self.c_phn = StringVar()
        self.c_bill = StringVar()
        x=random.randint(1,200)
        self.c_bill.set(str(x))
        self.search_bill = StringVar()



        f1 = LabelFrame(self.root,bd=10, relief=SUNKEN, text="CUSTOMER DETAILS", font=("times new roman",15,"bold"), fg="yellow", bg="black")
        f1.place(x=0, y=75, height=100, relwidth=1)
        cname_label = Label(f1, text="CUSTOMER NAME", bg="black", fg="white", font=("Courier",15)).grid(row=0,column=0,padx=20,pady=5)
        cname_entry = Entry(f1, width=20, bd=6, textvariable=self.c_name, relief=SUNKEN, font=("arial",15)).grid(row=0, column=1, padx=10, pady=5)

        cphn_label = Label(f1, text="PHONE NUMBER", bg="black", fg="white", font=("Courier",15)).grid(row=0,column=2,padx=20,pady=5)
        cphn_entry = Entry(f1, width=20, bd=6, relief=SUNKEN, textvariable=self.c_phn ,font=("arial",15)).grid(row=0, column=3, padx=10, pady=5)

        cbill_label = Label(f1, text="BILL NO.", bg="black", fg="white", font=("Courier",15)).grid(row=0,column=4,padx=20,pady=5)
        cbill_entry = Entry(f1, width=20, bd=6, relief=SUNKEN, textvariable=self.c_bill, font=("arial",15)).grid(row=0, column=5, padx=10, pady=5)

        


        f2 = LabelFrame(self.root,bd=10, relief=SUNKEN, text="PIZZAS", font=("times new roman",15,"bold"), fg="yellow", bg="black")
        f2.place(x=0, y=180, width=380, height=620)

        farmhouse = Label(f2, text="FARMHOUSE", bg="black", fg="white", font=("Courier",15)).grid(row=0,column=0, padx=10, pady=10, sticky="w")
        farmhouse_entry= Entry(f2, width=10, bd=6, textvariable=self.farmhouse_ , relief=SUNKEN, font=("arial",15)).grid(row=0, column=1, padx=10, pady=10)

        margherita = Label(f2, text="MARGHERITA", bg="black", fg="white", font=("Courier",15)).grid(row=1,column=0, padx=10, pady=10, sticky="w")
        margherita_entry= Entry(f2, width=10, bd=6, relief=SUNKEN, textvariable=self.margherita_ , font=("arial",15)).grid(row=1, column=1, padx=10, pady=10)

        capsicum = Label(f2, text="CAPSICUM", bg="black", fg="white", font=("Courier",15)).grid(row=2,column=0, padx=10, pady=10, sticky="w")
        capsicum_entry= Entry(f2, width=10, bd=6, relief=SUNKEN, textvariable=self.capsicum_ , font=("arial",15)).grid(row=2, column=1, padx=10, pady=10)

        pepperoni = Label(f2, text="PEPPERONI", bg="black", fg="white", font=("Courier",15)).grid(row=3,column=0, padx=10, pady=10, sticky="w")
        pep_entry= Entry(f2, width=10, bd=6, textvariable=self.pepperoni_ , relief=SUNKEN, font=("arial",15)).grid(row=3, column=1, padx=10, pady=10)

        brooklyn = Label(f2, text="BROOKLYN", bg="black", fg="white", font=("Courier",15)).grid(row=4,column=0, padx=10, pady=10, sticky="w")
        brooklyn_entry= Entry(f2, width=10, bd=6, textvariable=self.brooklyn_ , relief=SUNKEN, font=("arial",15)).grid(row=4, column=1, padx=10, pady=10)

        chargrilled = Label(f2, text="CHARGRILLED", bg="black", fg="white", font=("Courier",15)).grid(row=5,column=0, padx=10, pady=10, sticky="w")
        chargrilled_entry= Entry(f2, width=10, bd=6, textvariable=self.chargrilled_ , relief=SUNKEN, font=("arial",15)).grid(row=5, column=1, padx=10, pady=10)

        paneertikka = Label(f2, text="PANEER TIKKA", bg="black", fg="white", font=("Courier",15)).grid(row=6,column=0, padx=10, pady=10, sticky="w")
        paneertikka_entry= Entry(f2, width=10, bd=6, textvariable=self.paneertikka_ , relief=SUNKEN, font=("arial",15)).grid(row=6, column=1, padx=10, pady=10)

        mexican = Label(f2, text="MEXICAN", bg="black", fg="white", font=("Courier",15)).grid(row=7,column=0, padx=10, pady=10, sticky="w")
        mexican_entry= Entry(f2, width=10, bd=6, relief=SUNKEN, textvariable=self.mexican_ , font=("arial",15)).grid(row=7, column=1, padx=10, pady=10)

        pepper5 = Label(f2, text="5 PEPPER", bg="black", fg="white", font=("Courier",15)).grid(row=8,column=0, padx=10, pady=10, sticky="w")
        pepper5_entry= Entry(f2, width=10, bd=6, textvariable=self.pepper5_ , relief=SUNKEN, font=("arial",15)).grid(row=8, column=1, padx=10, pady=10)

        prawn = Label(f2, text="PRAWN", bg="black", fg="white", font=("Courier",15)).grid(row=9,column=0, padx=10, pady=10, sticky="w")
        prawn_entry= Entry(f2, width=10, bd=6, relief=SUNKEN, textvariable=self.prawn_ , font=("arial",15)).grid(row=9, column=1, padx=10, pady=10)


        
        f3 = LabelFrame(self.root,bd=10, relief=SUNKEN, text="SIDES", font=("times new roman",15,"bold"), fg="yellow", bg="black")
        f3.place(x=381, y=180, width=380, height=620)

        garlic_bread = Label(f3, text="GARLIC BREAD", bg="black", fg="white", font=("Courier",15)).grid(row=0,column=0, padx=10, pady=10, sticky="w")
        garlic_bread_entry= Entry(f3, width=10, bd=6, textvariable=self.garlic_bread_ , relief=SUNKEN, font=("arial",15)).grid(row=0, column=1, padx=10, pady=10)

        veg_wraps = Label(f3, text="VEG WRAPS", bg="black", fg="white", font=("Courier",15)).grid(row=1,column=0, padx=10, pady=10, sticky="w")
        veg_wraps_entry= Entry(f3, width=10, bd=6, relief=SUNKEN, textvariable=self.veg_wraps_ , font=("arial",15)).grid(row=1, column=1, padx=10, pady=10)

        non_veg_wraps = Label(f3, text="NON VEG WRAPS", bg="black", fg="white", font=("Courier",15)).grid(row=2,column=0, padx=10, pady=10, sticky="w")
        non_veg_wraps_entry= Entry(f3, width=10, bd=6, textvariable=self.non_veg_wraps_ , relief=SUNKEN, font=("arial",15)).grid(row=2, column=1, padx=10, pady=10)

        chicken_wings = Label(f3, text="CHICKEN WINGS", bg="black", fg="white", font=("Courier",15)).grid(row=3,column=0, padx=10, pady=10, sticky="w")
        chicken_wings_entry= Entry(f3, width=10, bd=6, textvariable=self.chicken_wings_ , relief=SUNKEN, font=("arial",15)).grid(row=3, column=1, padx=10, pady=10)

        veg_tacos = Label(f3, text="VEG TACOS", bg="black", fg="white", font=("Courier",15)).grid(row=4,column=0, padx=10, pady=10, sticky="w")
        veg_tacos_entry= Entry(f3, width=10, bd=6, relief=SUNKEN, textvariable=self.veg_tacos_ , font=("arial",15)).grid(row=4, column=1, padx=10, pady=10)

        non_tacos = Label(f3, text="NON VEG TACOS", bg="black", fg="white", font=("Courier",15)).grid(row=5,column=0, padx=10, pady=10, sticky="w")
        non_tacos_entry= Entry(f3, width=10, bd=6, textvariable=self.non_tacos_ , relief=SUNKEN, font=("arial",15)).grid(row=5, column=1, padx=10, pady=10)

        veg_burrito = Label(f3, text="VEG BURRITO", bg="black", fg="white", font=("Courier",15)).grid(row=6,column=0, padx=10, pady=10, sticky="w")
        veg_burrito_entry= Entry(f3, width=10, bd=6, textvariable=self.veg_burrito_ , relief=SUNKEN, font=("arial",15)).grid(row=6, column=1, padx=10, pady=10)

        non_veg_burrito = Label(f3, text="NON VEG BURRITO", bg="black", fg="white", font=("Courier",15)).grid(row=7,column=0, padx=10, pady=10, sticky="w")
        non_veg_burrito_entry= Entry(f3, width=10, bd=6, relief=SUNKEN, textvariable=self.non_veg_burrito_ , font=("arial",15)).grid(row=7, column=1, padx=10, pady=10)

        cheese_sticks = Label(f3, text="CHEESE STICKS", bg="black", fg="white", font=("Courier",15)).grid(row=8,column=0, padx=10, pady=10, sticky="w")
        cheese_sticks_entry= Entry(f3, width=10, bd=6, textvariable=self.cheese_sticks_ , relief=SUNKEN, font=("arial",15)).grid(row=8, column=1, padx=10, pady=10)

        fishnchips = Label(f3, text="FISH N CHIPS", bg="black", fg="white", font=("Courier",15)).grid(row=9,column=0, padx=10, pady=10, sticky="w")
        fishnchips_entry= Entry(f3, width=10, bd=6, textvariable=self.fishnchips_ , relief=SUNKEN, font=("arial",15)).grid(row=9, column=1, padx=10, pady=10)


        
        f4 = LabelFrame(self.root,bd=10, relief=SUNKEN, text="DESSERTS", font=("times new roman",15,"bold"), fg="yellow", bg="black")
        f4.place(x=762, y=180, width=380, height=620)

        chocolava = Label(f4, text="CHOCO LAVA CAKE", bg="black", fg="white", font=("Courier",15)).grid(row=0,column=0, padx=10, pady=10, sticky="w")
        chocolava_entry= Entry(f4, width=10, bd=6, textvariable=self.chocolava_ , relief=SUNKEN, font=("arial",15)).grid(row=0, column=1, padx=10, pady=10)

        cheesecake = Label(f4, text="CHEESECAKE", bg="black", fg="white", font=("Courier",15)).grid(row=1,column=0, padx=10, pady=10, sticky="w")
        cheesecake_entry= Entry(f4, width=10, bd=6, textvariable=self.cheesecake_ , relief=SUNKEN, font=("arial",15)).grid(row=1, column=1, padx=10, pady=10)

        brownie = Label(f4, text="BROWNIE", bg="black", fg="white", font=("Courier",15)).grid(row=2,column=0, padx=10, pady=10, sticky="w")
        brownie_entry= Entry(f4, width=10, bd=6, relief=SUNKEN, textvariable=self.brownie_ , font=("arial",15)).grid(row=2, column=1, padx=10, pady=10)

        sundae = Label(f4, text="SUNDAE", bg="black", fg="white", font=("Courier",15)).grid(row=3,column=0, padx=10, pady=10, sticky="w")
        sundae_entry= Entry(f4, width=10, bd=6, relief=SUNKEN, textvariable=self.sundae_ , font=("arial",15)).grid(row=3, column=1, padx=10, pady=10)

        choco_fudge = Label(f4, text="CHOCO FUDGE", bg="black", fg="white", font=("Courier",15)).grid(row=4,column=0, padx=10, pady=10, sticky="w")
        choco_fudge_entry= Entry(f4, width=10, bd=6, relief=SUNKEN, textvariable=self.choco_fudge_ , font=("arial",15)).grid(row=4, column=1, padx=10, pady=10)

        tiramisu = Label(f4, text="TIRAMISU", bg="black", fg="white", font=("Courier",15)).grid(row=5,column=0, padx=10, pady=10, sticky="w")
        tiramisu_entry= Entry(f4, width=10, bd=6, textvariable=self.tiramisu_ , relief=SUNKEN, font=("arial",15)).grid(row=5, column=1, padx=10, pady=10)

        pudding = Label(f4, text="PUDDING", bg="black", fg="white", font=("Courier",15)).grid(row=6,column=0, padx=10, pady=10, sticky="w")
        pudding_entry= Entry(f4, width=10, bd=6, textvariable=self.pudding_ , relief=SUNKEN, font=("arial",15)).grid(row=6, column=1, padx=10, pady=10)

        waffles = Label(f4, text="WAFFLES", bg="black", fg="white", font=("Courier",15)).grid(row=7,column=0, padx=10, pady=10, sticky="w")
        waffles_entry= Entry(f4, width=10, bd=6, relief=SUNKEN, textvariable=self.waffles_ , font=("arial",15)).grid(row=7, column=1, padx=10, pady=10)

        pancakes = Label(f4, text="PANCAKES", bg="black", fg="white", font=("Courier",15)).grid(row=8,column=0, padx=10, pady=10, sticky="w")
        pancakes_entry= Entry(f4, width=10, bd=6, relief=SUNKEN, textvariable=self.pancakes_ , font=("arial",15)).grid(row=8, column=1, padx=10, pady=10)

        carrot_cake = Label(f4, text="CARROT CAKE", bg="black", fg="white", font=("Courier",15)).grid(row=9,column=0, padx=10, pady=10, sticky="w")
        carrot_cake_entry= Entry(f4, width=10, bd=6, relief=SUNKEN, textvariable=self.carrot_cake_ , font=("arial",15)).grid(row=9, column=1, padx=10, pady=10)


        
        f5 = LabelFrame(self.root,bd=10, relief=SUNKEN, text="BEVERAGES", font=("times new roman",15,"bold"), fg="yellow", bg="black")
        f5.place(x=1143, y=180, width=380, height=620)

        pepsi = Label(f5, text="PEPSI", bg="black", fg="white", font=("Courier",15)).grid(row=0,column=0, padx=10, pady=10, sticky="w")
        pepsi_entry= Entry(f5, width=10, bd=6, relief=SUNKEN, textvariable=self.pepsi_ , font=("arial",15)).grid(row=0, column=1, padx=10, pady=10)

        coca_cola = Label(f5, text="COCA COLA", bg="black", fg="white", font=("Courier",15)).grid(row=1,column=0, padx=10, pady=10, sticky="w")
        coca_cola_entry= Entry(f5, width=10, bd=6, textvariable=self.coca_cola_ , relief=SUNKEN, font=("arial",15)).grid(row=1, column=1, padx=10, pady=10)

        fanta = Label(f5, text="FANTA", bg="black", fg="white", font=("Courier",15)).grid(row=2,column=0, padx=10, pady=10, sticky="w")
        fanta_entry= Entry(f5, width=10, bd=6, relief=SUNKEN, textvariable=self.fanta_ , font=("arial",15)).grid(row=2, column=1, padx=10, pady=10)

        fruit_juice = Label(f5, text="FRUIT JUICE", bg="black", fg="white", font=("Courier",15)).grid(row=3,column=0, padx=10, pady=10, sticky="w")
        fruit_juice_entry= Entry(f5, width=10, bd=6, relief=SUNKEN, textvariable=self.fruit_juice_ , font=("arial",15)).grid(row=3, column=1, padx=10, pady=10)

        sprite = Label(f5, text="SPRITE", bg="black", fg="white", font=("Courier",15)).grid(row=4,column=0, padx=10, pady=10, sticky="w")
        sprite_entry= Entry(f5, width=10, bd=6, relief=SUNKEN, textvariable=self.sprite_ , font=("arial",15)).grid(row=4, column=1, padx=10, pady=10)

        limca = Label(f5, text="LIMCA", bg="black", fg="white", font=("Courier",15)).grid(row=5,column=0, padx=10, pady=10, sticky="w")
        limca_entry= Entry(f5, width=10, bd=6, relief=SUNKEN, textvariable=self.limca_ , font=("arial",15)).grid(row=5, column=1, padx=10, pady=10)

        fruit_beer = Label(f5, text="FRUIT BEER", bg="black", fg="white", font=("Courier",15)).grid(row=6,column=0, padx=10, pady=10, sticky="w")
        fruit_beer_entry= Entry(f5, width=10, bd=6, relief=SUNKEN, textvariable=self.fruit_beer_ , font=("arial",15)).grid(row=6, column=1, padx=10, pady=10)

        frooti = Label(f5, text="FROOTI", bg="black", fg="white", font=("Courier",15)).grid(row=7,column=0, padx=10, pady=10, sticky="w")
        frooti_entry= Entry(f5, width=10, bd=6, relief=SUNKEN, textvariable=self.frooti_ , font=("arial",15)).grid(row=7, column=1, padx=10, pady=10)

        slice_ = Label(f5, text="SLICE", bg="black", fg="white", font=("Courier",15)).grid(row=8,column=0, padx=10, pady=10, sticky="w")
        slice_entry= Entry(f5, width=10, bd=6, relief=SUNKEN, textvariable=self.slice_1 , font=("arial",15)).grid(row=8, column=1, padx=10, pady=10)

        banta = Label(f5, text="BANTA", bg="black", fg="white", font=("Courier",15)).grid(row=9,column=0, padx=10, pady=10, sticky="w")
        banta_entry= Entry(f5, width=10, bd=6, relief=SUNKEN, textvariable=self.banta_ , font=("arial",15)).grid(row=9, column=1, padx=10, pady=10)

        


        f6 = LabelFrame(self.root,bd=10, relief=SUNKEN)
        f6.place(x=1524, y=180, width=385, height=620)
        bill_title = Label(f6, text="BILL", font=("arial", 15, "bold"), bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(f6, orient=VERTICAL)
        self.textarea = Text(f6, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)


        f7 = LabelFrame(self.root,bd=10, relief=SUNKEN, text="BILL AREA", font=("times new roman",15,"bold"), fg="yellow", bg="black")
        f7.place(x=0, y=805, relwidth=1, height=200)

        m1 = Label(f7, text="TOTAL PIZZAS PRICE",bg="black", fg="white", font=("Courier",15)).grid(row=0, column=0, padx=10, pady=1, sticky="w")
        m1_entry = Entry(f7, width="18", textvariable=self.pizzas_price , bd=7, relief=SUNKEN).grid(row=0,column=1,padx=10, pady=4)

        m2 = Label(f7, text="TOTAL SIDES PRICE",bg="black", fg="white", font=("Courier",15)).grid(row=1, column=0, padx=10, pady=1, sticky="w")
        m2_entry = Entry(f7, width="18", textvariable=self.sides_price , bd=7, relief=SUNKEN).grid(row=1,column=1,padx=10, pady=4)

        m3 = Label(f7, text="TOTAL DESSERTS PRICE",bg="black", fg="white", font=("Courier",15)).grid(row=2, column=0, padx=10, pady=1, sticky="w")
        m3_entry = Entry(f7, width="18", bd=7, textvariable=self.desserts_price , relief=SUNKEN).grid(row=2,column=1,padx=10, pady=4)

        m4 = Label(f7, text="TOTAL BEVERAGES PRICE",bg="black", fg="white", font=("Courier",15)).grid(row=3, column=0, padx=10, pady=1, sticky="w")
        m4_entry = Entry(f7, width="18", bd=7, textvariable=self.beverages_price , relief=SUNKEN).grid(row=3,column=1,padx=10, pady=4)

        c1 = Label(f7, text="PIZZAS TAX",bg="black", fg="white", font=("Courier",15)).grid(row=0, column=2, padx=10, pady=1, sticky="w")
        c1_entry = Entry(f7, width="18", textvariable=self.pizzas_tax , bd=7, relief=SUNKEN).grid(row=0,column=3,padx=10, pady=4)

        c2 = Label(f7, text="SIDES TAX",bg="black", fg="white", font=("Courier",15)).grid(row=1, column=2, padx=10, pady=1, sticky="w")
        c2_entry = Entry(f7, width="18", textvariable=self.sides_tax , bd=7, relief=SUNKEN).grid(row=1,column=3,padx=10, pady=4)

        c3 = Label(f7, text="DESSERTS TAX",bg="black", fg="white", font=("Courier",15)).grid(row=2, column=2, padx=10, pady=1, sticky="w")
        c3_entry = Entry(f7, width="18", textvariable=self.desserts_tax , bd=7, relief=SUNKEN).grid(row=2,column=3,padx=10, pady=4)

        c4 = Label(f7, text="BEVERAGES TAX",bg="black", fg="white", font=("Courier",15)).grid(row=3, column=2, padx=10, pady=1, sticky="w")
        c4_entry = Entry(f7, width="18", textvariable=self.beverages_tax , bd=7, relief=SUNKEN).grid(row=3,column=3,padx=10, pady=4)

       

        button_frame = Frame(f7, bd=7, relief=SUNKEN)
        button_frame.place(x=770, y=30, width= 842, height=100)

        total_button = Button(button_frame, command=self.total, text="TOTAL", bd=5, bg="cadetblue", fg="black", pady=15, width=15, font=("Courier",15)).grid(row=0, column=0, padx=5, pady=5)

        generate_button = Button(button_frame, text="GENERATE BILL", command=self.bill_area , bd=5, bg="cadetblue", fg="black", pady=15, width=15, font=("Courier",15)).grid(row=0, column=1, padx=5, pady=5)

        clear_button = Button(button_frame, text="CLEAR", bd=5, bg="cadetblue", command=self.clear_data, fg="black", pady=15, width=15, font=("Courier",15)).grid(row=0, column=2, padx=5, pady=5)

        exit_button = Button(button_frame, text="EXIT", bd=5, bg="cadetblue", command=self.exit_app, fg="black", pady=15, width=15, font=("Courier",15)).grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()
    
    def total(self):

        self.p_farm_p = self.farmhouse_.get()*50
        self.p_marg_p = self.margherita_.get()*60
        self.p_cap_p = self.capsicum_.get()*70
        self.p_pep_p = self.pepperoni_.get()*80
        self.p_brook_p = self.brooklyn_.get()*90 
        self.p_charg_p = self.chargrilled_.get()*100
        self.p_paneer_p = self.paneertikka_.get()*110 
        self.p_mex_p = self.mexican_.get()*120
        self.p_pepper_p = self.pepper5_.get()*130
        self.p_prawn_p = self.prawn_.get()*140 

        self.total_pizzas_price=float( 
                                    self.p_farm_p+
                                    self.p_marg_p+
                                    self.p_cap_p+
                                    self.p_pep_p+
                                    self.p_brook_p+
                                    self.p_charg_p+
                                    self.p_paneer_p+
                                    self.p_mex_p+
                                    self.p_pepper_p+
                                    self.p_prawn_p
                                    ) 
        self.pizzas_price.set("Rs. "+str(self.total_pizzas_price))
        self.p_tax = round((self.total_pizzas_price*0.18),2)
        self.pizzas_tax.set("Rs. "+str(self.p_tax))

        self.s_gar_p = self.garlic_bread_.get()*10
        self.s_vwrap_p = self.veg_wraps_.get()*20
        self.s_nwrap_p = self.non_veg_wraps_.get()*25
        self.s_cwings_p = self.chicken_wings_.get()*40
        self.s_vtaco_p = self.veg_tacos_.get()*30
        self.s_ntaco_p = self.non_tacos_.get()*35
        self.s_vburr_p = self.veg_burrito_.get()*50
        self.s_nburr_p = self.non_veg_burrito_.get()*55
        self.s_chesti_p = self.cheese_sticks_.get()*20
        self.s_fnchip_p = self.fishnchips_.get()*60
       

        self.total_sides_price=float(
                                    self.s_gar_p+
                                    self.s_vwrap_p+ 
                                    self.s_nwrap_p+ 
                                    self.s_cwings_p+ 
                                    self.s_vtaco_p+ 
                                    self.s_ntaco_p+
                                    self.s_vburr_p+ 
                                    self.s_nburr_p+
                                    self.s_chesti_p+
                                    self.s_fnchip_p
                                    )
        self.sides_price.set("Rs. "+str(self.total_sides_price))
        self.s_tax = round((self.total_sides_price*0.18),2)
        self.sides_tax.set("Rs. "+str(self.s_tax))


        self.d_clava_p = self.chocolava_.get()*20
        self.d_checak_p = self.cheesecake_.get()*30
        self.d_brown_p = self.brownie_.get()*20
        self.d_sun_p = self.sundae_.get()*50
        self.d_cfuge_p = self.choco_fudge_.get()*40
        self.d_tira_p = self.tiramisu_.get()*70
        self.d_pudd_p = self.pudding_.get()*40
        self.d_waff_p = self.waffles_.get()*50
        self.d_panc_p = self.pancakes_.get()*50
        self.d_carcak_p = self.carrot_cake_.get()*60
        

        self.total_desserts_price=float(
                                        self.d_clava_p+
                                        self.d_checak_p+
                                        self.d_brown_p+
                                        self.d_sun_p+
                                        self.d_cfuge_p+
                                        self.d_tira_p+
                                        self.d_pudd_p+
                                        self.d_waff_p+
                                        self.d_panc_p+
                                        self.d_carcak_p
                                       )
        self.desserts_price.set("Rs. "+str(self.total_desserts_price))
        self.d_tax = round((self.total_desserts_price*0.18),2)
        self.desserts_tax.set("Rs. "+str(self.d_tax))
        

        self.b_pepsi_p = self.pepsi_.get()*30
        self.b_coke_p = self.coca_cola_.get()*30
        self.b_fanta_p = self.fanta_.get()*30
        self.b_fruitj_p = self.fruit_juice_.get()*30
        self.b_sprite_p = self.sprite_.get()*30
        self.b_limca_p = self.limca_.get()*30
        self.b_fruitb_p = self.fruit_beer_.get()*40
        self.b_frooti_p = self.frooti_.get()*30
        self.b_slice_p = self.slice_1.get()*30
        self.b_banta_p = self.banta_.get()*20

        self.total_beverages_price=float(
                                        self.b_pepsi_p+ 
                                        self.b_coke_p+
                                        self.b_fanta_p+
                                        self.b_fruitj_p+
                                        self.b_sprite_p+
                                        self.b_limca_p+
                                        self.b_fruitb_p+
                                        self.b_frooti_p+
                                        self.b_slice_p+
                                        self.b_banta_p
                                        )
        self.beverages_price.set("Rs. "+str(self.total_beverages_price))
        self.b_tax = round((self.total_beverages_price*0.18),2)
        self.beverages_tax.set("Rs. "+str(self.b_tax))

        self.total_bill = float(
                                round((
                                self.total_pizzas_price+
                                self.total_sides_price+
                                self.total_desserts_price+
                                self.total_beverages_price+
                                self.p_tax+
                                self.s_tax+
                                self.d_tax+
                                self.b_tax),2)
                               )
    

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "\tLA BENNETT PIZZA,GREATER NOIDA")
        self.textarea.insert(END, f"\n\nBILL NO: {self.c_bill.get()}")
        self.textarea.insert(END, f"\nCUSTOMER NAME: {self.c_name.get()}")
        self.textarea.insert(END, f"\nPHONE NUMBER: {self.c_phn.get()}")
        self.textarea.insert(END, f"\n===========================================")
        self.textarea.insert(END, f"\n ITEMS\t\t   QTY\t\t   PRICE")
        self.textarea.insert(END, f"\n===========================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phn.get()=="":
            messagebox.showerror("ERROR","ALL CUSTOMER DETAILS ARE REQUIRED")
        elif self.pizzas_price.get()=="Rs. 0.0" and self.sides_price.get()=="Rs. 0.0" and self.desserts_price.get()=="Rs. 0.0" and self.beverages_price.get()=="Rs. 0.0":
            messagebox.showerror("ERROR","NO ITEM WAS SELECTED")
        else:
            self.welcome_bill()
            #====pizzas
            if self.farmhouse_.get()!=0:
                self.textarea.insert(END, f"\n FARMHOUSE\t\t    {self.farmhouse_.get()}\t\t   Rs.{self.p_farm_p}")
            if self.margherita_.get()!=0:
                self.textarea.insert(END, f"\n MARGHERITA\t\t    {self.margherita_.get()}\t\t   Rs.{self.p_marg_p}")
            if self.capsicum_.get()!=0:
                self.textarea.insert(END, f"\n CAPSICUM\t\t    {self.capsicum_.get()}\t\t   Rs.{self.p_cap_p}")
            if self.pepperoni_.get()!=0:
                self.textarea.insert(END, f"\n PEPPERONI\t\t    {self.pepperoni_.get()}\t\t   Rs.{self.p_pep_p}")
            if self.brooklyn_.get()!=0:
                self.textarea.insert(END, f"\n BROOKLYN\t\t    {self.brooklyn_.get()}\t\t   Rs.{self.p_brook_p}")
            if self.chargrilled_.get()!=0:
                self.textarea.insert(END, f"\n CHARGRILLED\t\t    {self.chargrilled_.get()}\t\t   Rs.{self.p_charg_p}")
            if self.paneertikka_.get()!=0:
                self.textarea.insert(END, f"\n PANEER TIKKA\t\t    {self.paneertikka_.get()}\t\t   Rs.{self.p_paneer_p}")
            if self.mexican_.get()!=0:
                self.textarea.insert(END, f"\n MEXICAN\t\t    {self.mexican_.get()}\t\t   Rs.{self.p_mex_p}")
            if self.pepper5_.get()!=0:
                self.textarea.insert(END, f"\n 5 PEPPER\t\t    {self.pepper5_.get()}\t\t   Rs.{self.p_pepper_p}")
            if self.prawn_.get()!=0:
                self.textarea.insert(END, f"\n PRAWN\t\t    {self.prawn_.get()}\t\t   Rs.{self.p_prawn_p}")

            #======sides
            if self.garlic_bread_.get()!=0:
                self.textarea.insert(END, f"\n GARLIC BREAD\t\t    {self.garlic_bread_.get()}\t\t   Rs.{self.s_gar_p}")
            if self.veg_wraps_.get()!=0:
                self.textarea.insert(END, f"\n VEG WRAPS\t\t    {self.veg_wraps_.get()}\t\t   Rs.{self.s_vwrap_p}")
            if self.non_veg_wraps_.get()!=0:
                self.textarea.insert(END, f"\n NON VEG WRAPS\t\t    {self.non_veg_wraps_.get()}\t\t   Rs.{self.s_nwrap_p}")
            if self.chicken_wings_.get()!=0:
                self.textarea.insert(END, f"\n CHICKEN WINGS\t\t    {self.chicken_wings_.get()}\t\t   Rs.{self.s_cwings_p}")
            if self.veg_tacos_.get()!=0:
                self.textarea.insert(END, f"\n VEG TACOS\t\t    {self.veg_tacos_.get()}\t\t   Rs.{self.s_vtaco_p}")
            if self.non_tacos_.get()!=0:
                self.textarea.insert(END, f"\n NON VEG TACOS\t\t    {self.non_tacos_.get()}\t\t   Rs.{self.s_ntaco_p}")
            if self.veg_burrito_.get()!=0:
                self.textarea.insert(END, f"\n VEG BURRITO\t\t    {self.veg_burrito_.get()}\t\t   Rs.{self.s_vburr_p}")
            if self.non_veg_burrito_.get()!=0:
                self.textarea.insert(END, f"\n NON VEG BURRITO\t\t    {self.non_veg_burrito_.get()}\t\t   Rs.{self.s_nburr_p}")
            if self.cheese_sticks_.get()!=0:
                self.textarea.insert(END, f"\n CHEESE STICKS\t\t    {self.cheese_sticks_.get()}\t\t   Rs.{self.s_chesti_p}")
            if self.fishnchips_.get()!=0:
                self.textarea.insert(END, f"\n FISH N CHIPS\t\t    {self.fishnchips_.get()}\t\t   Rs.{self.s_fnchip_p}")

            #====desserts
            if self.chocolava_.get()!=0:
                self.textarea.insert(END, f"\n CHOCOLAVA\t\t    {self.chocolava_.get()}\t\t   Rs.{self.d_clava_p}")
            if self.cheesecake_.get()!=0:
                self.textarea.insert(END, f"\n CHEESECAKE\t\t    {self.cheesecake_.get()}\t\t   Rs.{self.d_checak_p}")
            if self.brownie_.get()!=0:
                self.textarea.insert(END, f"\n BROWNIE\t\t    {self.brownie_.get()}\t\t   Rs.{self.d_brown_p}")
            if self.sundae_.get()!=0:
                self.textarea.insert(END, f"\n SUNDAE\t\t    {self.sundae_.get()}\t\t   Rs.{self.d_sun_p}")
            if self.choco_fudge_.get()!=0:
                self.textarea.insert(END, f"\n CHOCO FUDGE\t\t    {self.choco_fudge_.get()}\t\t   Rs.{self.d_cfuge_p}")
            if self.tiramisu_.get()!=0:
                self.textarea.insert(END, f"\n TIRAMISE\t\t    {self.tiramisu_.get()}\t\t   Rs.{self.d_tira_p}")
            if self.pudding_.get()!=0:
                self.textarea.insert(END, f"\n PUDDING\t\t    {self.pudding_.get()}\t\t   Rs.{self.d_pudd_p}")
            if self.waffles_.get()!=0:
                self.textarea.insert(END, f"\n WAFFLES\t\t    {self.waffles_.get()}\t\t   Rs.{self.d_waff_p}")
            if self.pancakes_.get()!=0:
                self.textarea.insert(END, f"\n PANCAKES\t\t    {self.pancakes_.get()}\t\t   Rs.{self.d_panc_p}")
            if self.carrot_cake_.get()!=0:
                self.textarea.insert(END, f"\n CARROT CAKE\t\t    {self.carrot_cake_.get()}\t\t   Rs.{self.d_carcak_p}")

            #====beverages
            if self.pepsi_.get()!=0:
                self.textarea.insert(END, f"\n PEPSI\t\t    {self.pepsi_.get()}\t\t   Rs.{self.b_pepsi_p}")
            if self.coca_cola_.get()!=0:
                self.textarea.insert(END, f"\n COCA COLA\t\t    {self.coca_cola_.get()}\t\t   Rs.{self.b_coke_p}")
            if self.fanta_.get()!=0:
                self.textarea.insert(END, f"\n FANTA\t\t    {self.fanta_.get()}\t\t   Rs.{self.b_fanta_p}")
            if self.fruit_juice_.get()!=0:
                self.textarea.insert(END, f"\n FRUIT JUICE\t\t    {self.fruit_juice_.get()}\t\t   Rs.{self.b_fruitj_p}")
            if self.sprite_.get()!=0:
                self.textarea.insert(END, f"\n SPRITE\t\t    {self.sprite_.get()}\t\t   Rs.{self.b_sprite_p}")
            if self.limca_.get()!=0:
                self.textarea.insert(END, f"\n LIMCA\t\t    {self.limca_.get()}\t\t   Rs.{self.b_limca_p}")
            if self.fruit_beer_.get()!=0:
                self.textarea.insert(END, f"\n FRUIT BEER\t\t    {self.fruit_beer_.get()}\t\t   Rs.{self.b_fruitb_p}")
            if self.frooti_.get()!=0:
                self.textarea.insert(END, f"\n FROOTI\t\t    {self.frooti_.get()}\t\t   Rs.{self.b_frooti_p}")
            if self.slice_1.get()!=0:
                self.textarea.insert(END, f"\n SLICE\t\t    {self.slice_1.get()}\t\t   Rs.{self.b_slice_p}")
            if self.banta_.get()!=0:
                self.textarea.insert(END, f"\n BANTA\t\t    {self.banta_.get()}\t\t   Rs.{self.b_banta_p}")


            self.textarea.insert(END, f"\n-------------------------------------------")
            if self.pizzas_tax.get()!="Rs. 0.0":
                self.textarea.insert(END, f"\nPIZZAS TAX\t\t\t\t  {self.pizzas_tax.get()}")
            if self.sides_tax.get()!="Rs. 0.0":
                self.textarea.insert(END, f"\nSIDES TAX\t\t\t\t  {self.sides_tax.get()}")
            if self.desserts_tax.get()!="Rs. 0.0":
                self.textarea.insert(END, f"\nDESSERTS TAX\t\t\t\t  {self.desserts_tax.get()}")
            if self.beverages_tax.get()!="Rs. 0.0":
                self.textarea.insert(END, f"\nBEVERAGES TAX\t\t\t\t  {self.beverages_tax.get()}")
            self.textarea.insert(END, f"\nTOTAL AMOUNT\t\t\t\t  Rs.{self.total_bill}")
            self.textarea.insert(END, f"\n-------------------------------------------")
            self.save_bill()

        
    def save_bill(self):
        op=messagebox.askyesno("SAVE BILL","SAVE THE BILL?")
        if op>0:
            self.bill_data = self.textarea.get('1.0',END)
            save = open("E:/BILLING SYSTEM NEW/bills/"+str(self.c_bill.get())+".txt","w")
            save.write(self.bill_data)
            save.close()
            messagebox.showinfo("SAVED",f"BILL NO.{self.c_bill.get()} HAS BEEN SAVED")
        else:
            return
    


    def clear_data(self):
        op=messagebox.askyesno("CLEAR","DO YOU WANT TO CLEAR THE DATA?")
        if op>0:
            self.farmhouse_.set(0)
            self.margherita_.set(0)
            self.capsicum_.set(0)
            self.pepperoni_.set(0)
            self.brooklyn_.set(0)
            self.chargrilled_.set(0)
            self.paneertikka_.set(0)
            self.mexican_.set(0)
            self.pepper5_.set(0)
            self.prawn_.set(0)

            self.garlic_bread_.set(0)
            self.veg_wraps_.set(0)
            self.non_veg_wraps_.set(0)
            self.chicken_wings_.set(0)
            self.veg_tacos_.set(0)
            self.non_tacos_.set(0)
            self.veg_burrito_.set(0)
            self.non_veg_burrito_.set(0)
            self.cheese_sticks_.set(0)
            self.fishnchips_.set(0)

            self.chocolava_.set(0)
            self.cheesecake_.set(0)
            self.brownie_.set(0)
            self.sundae_.set(0)
            self.choco_fudge_.set(0)
            self.tiramisu_.set(0)
            self.pudding_.set(0)
            self.waffles_.set(0)
            self.pancakes_.set(0)
            self.carrot_cake_.set(0)

            self.pepsi_.set(0)
            self.coca_cola_.set(0)
            self.fanta_.set(0)
            self.fruit_juice_.set(0)
            self.sprite_.set(0)
            self.limca_.set(0)
            self.fruit_beer_.set(0)
            self.frooti_.set(0)
            self.slice_1.set(0)
            self.banta_.set(0)

            self.pizzas_price.set("")
            self.sides_price.set("") 
            self.desserts_price.set("")
            self.beverages_price.set("")

            self.pizzas_tax.set("")
            self.sides_tax.set("")
            self.desserts_tax.set("")
            self.beverages_tax.set("")

            self.c_name.set("")
            self.c_phn.set("")
            self.c_bill.set("")
            x=random.randint(1,200)
            self.c_bill.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()


    def exit_app(self):
        op=messagebox.askyesno("EXIT","DO YOU WANT TO EXIT?")
        if op>0:
            self.root.destroy()


        
root = Tk()
obj = bill_app(root)
root.mainloop()