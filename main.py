class card:
    cards_list = []
    c_r = None
    c_g = None
    c_b = None
    @staticmethod
    def calc_closest(c):                
        c_dict = {'r':card.c_r,'g':card.c_g,'b':card.c_b}
        for k,v in c_dict.items():            
            for i in range(len(v)):
                if v[i]==c:
                    try:
                        cw = v[i+1].colors[k]
                    except:
                        cw = v[0].colors[k]
                    try:
                        ccw = v[i-1].colors[k]
                    except:
                        ccw = v[-1].colors[k]
                    c.closest_cw[k] = cw
                    c.closest_ccw[k] = ccw
                    break
    def __init__(self,k):
        self.colors = {'r':k[0],'g':k[1],'b':k[2]}
        self.id = k[3]
        self.u_colors = {'r':None,'g':None,'b':None}
        self.u = None        
        self.closest_cw = {'r':None,'g':None,'b':None}
        self.closest_ccw = {'r':None,'g':None,'b':None}
        card.cards_list.append(self)
        c = card.cards_list
        card.c_r = c.copy()
        card.c_g = c.copy()
        card.c_b = c.copy()
        card.c_r.sort(key=lambda x:x.colors['r'])
        card.c_g.sort(key=lambda x:x.colors['g'])
        card.c_b.sort(key=lambda x:x.colors['b'])
    def __eq__(self,other):
        return self.id == other.id
    def calc(self):
        self.u = sum(self.u_colors.values())    

    def calc_uniqueness(self):
        colors = ['r','g','b']
        for color in colors:            
            angle = self.colors[color]
            cw_cl = self.closest_cw[color]
            ccw_cl = self.closest_ccw[color]
            if(cw_cl>angle):
                r = cw_cl-angle
            elif(cw_cl==angle):
                r = 0
            else:
                r = 360 - angle + cw_cl
            if(ccw_cl<angle):
                r+= angle-ccw_cl
            elif(ccw_cl==angle):
                r += 0
            else:
                r+= 360 - ccw_cl + angle
            self.u_colors[color] = r
        self.calc();

# card([0,0,0,0])
# card([120,120,120,120])
# card([240,240,240,240])
# card([0,120,240,2017])

# card([42,1,1,1])
# card([90,1,1,2])
# card([110,1,1,3])



def run():    
    id_list = []
    while len(card.cards_list)>0:    
        for c in card.cards_list:    
            card.calc_closest(c)
            c.calc_uniqueness()
        final_cards = card.cards_list
        final_cards.sort(key=lambda x:x.id,reverse=True)
        final_cards.sort(key=lambda x:x.u)    
        c = final_cards.pop(0);
        id_list.append(c.id);
    print(id_list)

i = int(input())
for j in range(i):
    k = input()
    k = [int(l) for l in k.split()]
    card(k);
run()