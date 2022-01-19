from cita import cita
from PIL import Image

app = cita()

munif_img1 = Image.open("known_faces/munif/269889616_336306334993491_7379000249664606489_n.jpg")
munif_img2 = Image.open("known_faces/munif/271329567_340643287893129_1772680651404513355_n.jpg")
munif_imgs = [munif_img1, munif_img2]



ortha_img = Image.open("known_faces/ortha/243360778_570892687584853_8624198295529905887_n.jpg")
ortha_imgs = [ortha_img,]


rifat_img1 = Image.open("known_faces/rifat/140722866_861559914606312_2043020816294231298_n.jpg")
rifat_img2 = Image.open("known_faces/rifat/142444225_862152351213735_3386904579733135234_n.jpg")
rifat_imgs = [rifat_img1, rifat_img2]


app.register_entry(ortha_imgs, "Ortha", "ortha@gmail.com", "Kotkipara", "01555", 90)
app.register_entry(munif_imgs, "Munif", "munif@gmail.com", "Keranipara", "01755", 15)
app.register_entry(rifat_imgs, "Rifat", "rifat@gmail.com", "Kijani", "999", 20)



test_img = Image.open("unknown_faces/265025206_323815426242582_7407026420439637180_n.jpg") 
print(app.check_entry(test_img))
