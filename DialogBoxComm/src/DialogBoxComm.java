/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.HBox;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;
import javafx.stage.Stage;

/**
 *
 * @author Carlotta
 */
public class DialogBoxComm extends Application {
    VBox vbox;
    HBox hb;
    Text text1;
    MyButton foto;
    MyButton video;
    @Override
    public void start(Stage primaryStage) {
        vbox = new VBox();
        text1 = new Text("Vuoi modificare la foto o il video? ");
        hb = new HBox();
        foto = new MyButton("foto", false, new photoListener(primaryStage));
        video = new MyButton("video", false, new videoListener(primaryStage));
        hb.getChildren().addAll(foto, video);
        hb.setAlignment(Pos.CENTER);
        hb.setSpacing(10);
        vbox.getChildren().addAll(text1, hb);
        vbox.setAlignment(Pos.CENTER);
        vbox.setSpacing(20);
        
        Scene scene = new Scene(vbox, 300, 250);
        
        primaryStage.setTitle("applica filtri");
        primaryStage.setScene(scene);
        primaryStage.sizeToScene();
        primaryStage.show();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }
    class photoListener implements EventHandler<MouseEvent>{
        Stage stageUno;
        public photoListener(Stage stage){
            this.stageUno = stage;
        }
        @Override
        public void handle(MouseEvent event){
            stageUno.close();
            new EsaComm().show();
        }
    }
    class videoListener implements EventHandler<MouseEvent>{
        Stage stageUno;
        public videoListener(Stage stage){
            this.stageUno = stage;
        }
        @Override
        public void handle(MouseEvent event){
            stageUno.close();
            new EsaComm().show();
        }
    }
    
}
