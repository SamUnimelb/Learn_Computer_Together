package pkg01_hellojfx;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.MouseEvent;

/**
 * FXML Controller class
 *
 * @author Sam_Yan
 */
public class FXMLController implements Initializable {

    private boolean entered;
    @FXML
    private Button pageBt;
    @FXML
    private Label infoLabel;

    /**
     * Initializes the controller class.
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        entered = false;
    }    

    @FXML
    private void pageBtClicked(MouseEvent event) {
        if(entered){
            pageBt.setText("再见");
            infoLabel.setText("欢迎下次光临！");
        }else{
            pageBt.setText("进入");
            infoLabel.setText("欢迎光临！");
        }
        
        entered = !entered;
    }
    
}
