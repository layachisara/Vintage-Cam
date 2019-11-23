
import javafx.event.EventHandler;
import javafx.scene.control.Button;
import javafx.scene.input.MouseEvent;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Carlotta
 */
public class MyButton extends Button {
    public MyButton(String label, boolean isDisabled, EventHandler listener){
        super(label);
        setMinSize(60,60);
        setDisable(isDisabled);
        addEventHandler(MouseEvent.MOUSE_PRESSED, listener);
    }
}
