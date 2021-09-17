/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package pkg01_hellojfx;

import java.io.IOException;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
/**
 * To run this file, add VM run / compliation options:
 * --module-path "C:\Develop_Tools\Java\javafx-sdk-11.0.2\lib" --add-modules javafx.controls,javafx.fxml
 * @author Sam_Yan
 */
public class FXMain extends Application {

    @Override
    public void start(Stage primaryStage) throws IOException {

        Parent root = FXMLLoader.load(getClass().getResource("/pkg01_hellojfx/FXML.fxml"));
        Scene scene = new Scene(root);
        
        primaryStage.setTitle("智能迎客牌");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }

}
