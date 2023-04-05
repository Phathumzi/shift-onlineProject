package com.example.javafxdemo;

import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.AnchorPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

import java.io.IOException;


public class Checkers extends Application {
    @Override
    public void start(Stage stage) throws IOException {


        AnchorPane pane = new AnchorPane();
        Scene scene = new Scene(pane);
        stage.setScene(scene);

        int columns = 8, row = 8, horizontal = 80, vertical = 80;
        Rectangle rectangle = null;
        for(int i = 0; i < 8; i++){
            for(int j = 0; j < 8; j++){
                //creates the rectangles, and outlines them
                rectangle = new Rectangle(horizontal*j, vertical*i, horizontal, vertical);
                rectangle.setStroke(Color.WHITE);
                Rectangle finalRectangle = rectangle;
                if (( j+i) % 2 == 0 ) {
                    rectangle.setFill(Color.WHITE);

                }
                else {
                    rectangle.setFill(Color.BLACK);
                }//end else

                //put rectangles into the pane
                pane.getChildren().add(rectangle);

                    //sets the rectangles to be clickable
                    rectangle.setOnMouseClicked(new EventHandler<MouseEvent>() {
                        @Override
                        public void handle(MouseEvent mouseEvent) {
                            if (finalRectangle.getFill().equals(Color.BLACK)) { //Black tiles to return valid move
                            System.out.println(finalRectangle.getX() + " " + finalRectangle.getY());
                            }

                            else if (finalRectangle.getFill().equals(Color.WHITE)) { //White rectangles to return invalid move
                                System.out.println("Invalid Move");
                            }
                        }
                    });


            }//end for-loop j
        }//end for-loop i

        //create a scene and place it in the stage
        scene.setRoot(pane);
        stage.setTitle("Checkerboard");
        stage.show();
    }



    public static void main(String[] args) {
        launch();
    }



}