
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.stage.Stage;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Carlotta
 */
public class EsaComm extends Stage {

    public EsaComm(){
        Image image = new Image("file:\\Users\\Carlotta\\Documents\\UNIVERSITA'\\TERZO ANNO\\comunicazioni multimediali\\party-compleanno-e1462652810200.jpg", 500, 500, true, true);
        ImageView iw = new ImageView(image);
        Group root = new Group(iw);
        iw.setX(100);
        Scene scene = new Scene(root, 650,650);
        setTitle("Festa di compleanno");
        setScene(scene);
        sizeToScene();
        show();
    }
    
}
