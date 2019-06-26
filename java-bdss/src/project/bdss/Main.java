package project.bdss;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.SwingConstants;
import javax.swing.text.DateFormatter;
import javax.swing.text.DefaultFormatterFactory;

import org.python.util.PythonInterpreter;

import processing.core.PApplet;
import project.bdss.data.Coordinate;
import project.bdss.data.STTrajectoryEntity;

import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

import java.awt.Font;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFormattedTextField;

import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.URISyntaxException;
import java.net.URL;
import java.security.InvalidKeyException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.awt.event.ActionEvent;
import java.awt.CardLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import javax.swing.JTextField;
import g4p_controls.*;
import java.awt.TextArea;

public class Main {

	private JFrame frame;
	private JPanel mainPanel;
	private JPanel homePanel;
	private JPanel insertPanel;
	private JPanel queryPanel;
	private CardLayout cl;
	private JButton btnInsert;
	private JButton btnQuery;
	private JButton btnHome;
	private JLabel lblTitle;
	private JLabel lblFooter;
	private JButton btnUpload;
	private JLabel lblResponse;
	private JFormattedTextField tfStartTime;
	private JTextField tfDuration;
	private JTextField tfEdge;
	private Connection con;
	private JLabel lblStartTime;
	private JLabel lblDuration;
	private JLabel lblEdge;
	private TextArea taLatLong;
	private JButton btnSearch;
	private List<String> selected_edge;
	private Set<String> set;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Main window = new Main();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 * @throws URISyntaxException 
	 * @throws InvalidKeyException 
	 */
	public Main() throws InvalidKeyException, URISyntaxException {
		con = new Connection();
		con.Initialize();
		con.ListTable();
		
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(0, 0, 800, 600);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		frame.getContentPane().setBackground(Color.BLACK);
		
		mainPanel = new JPanel();
		mainPanel.setBounds(100, 0, 684, 560);
		frame.getContentPane().add(mainPanel);
		
		cl = new CardLayout(0, 0);
		mainPanel.setLayout(cl);

		homePanel = new JPanel();
		homePanel.setBackground(Color.WHITE);
		homePanel.setLayout(null);
		
		insertPanel = new JPanel();
		insertPanel.setBackground(Color.WHITE);		
		insertPanel.setLayout(null);
		
		queryPanel = new JPanel();
		queryPanel.setBackground(Color.WHITE);
		queryPanel.setLayout(null);
		
		mainPanel.add(homePanel, "0");
		mainPanel.add(insertPanel, "1");
		mainPanel.add(queryPanel, "2");
		
		cl.show(mainPanel, "0");
		
		SidePanel();
		HomePanel();
		QueryPanel();
		InsertPanel();
	}
	
	public void SidePanel() {
		JLabel lblReachabilityQueryApplication = new JLabel("<html><div style='text-align: center;'>Reachability Query<br>Application</div></html>");
		lblReachabilityQueryApplication.setForeground(Color.WHITE);
		lblReachabilityQueryApplication.setBounds(0, 100, 100, 100);
		lblReachabilityQueryApplication.setHorizontalAlignment(SwingConstants.CENTER);
		lblReachabilityQueryApplication.setFont(new Font("Gulim", Font.BOLD, 18));
		frame.getContentPane().add(lblReachabilityQueryApplication);
		
		btnHome = new JButton("HOME");
		btnHome.setBackground(Color.BLUE);
		btnHome.setForeground(Color.WHITE);
		btnHome.setFont(new Font("Gulim", Font.BOLD, 16));
		btnHome.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				cl.show(mainPanel, "0");
			}
		});
		btnHome.setBounds(5, 250, 90, 50);
		frame.getContentPane().add(btnHome);
		
		btnInsert = new JButton("INSERT");
		btnInsert.setBackground(Color.BLUE);
		btnInsert.setForeground(Color.WHITE);
		btnInsert.setFont(new Font("Gulim", Font.BOLD, 16));
		btnInsert.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				cl.show(mainPanel, "1");
			}
		});
		btnInsert.setBounds(5, 350, 90, 50);
		frame.getContentPane().add(btnInsert);
		
		btnQuery = new JButton("QUERY");
		btnQuery.setBackground(Color.BLUE);
		btnQuery.setForeground(Color.WHITE);
		btnQuery.setFont(new Font("Gulim", Font.BOLD, 16));
		btnQuery.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				cl.show(mainPanel, "2");
			}
		});
		btnQuery.setBounds(5, 450, 90, 50);
		frame.getContentPane().add(btnQuery);
	}
	
	public void HomePanel() {
		lblTitle = new JLabel("<html><div style='text-align: center;'>Cloud-Based Distributed System For Mining Spatio-Temporal Reachable Regions "
				+ "over Massive Trajectory Data<br><br><br>Steven Kurniawan - 201983296<br>Rian Danis Adi Pratama - 201999140</div></html>");
		lblTitle.setFont(new Font("Gulim", Font.BOLD, 18));
		lblTitle.setBounds(50, 180, 600, 200);
		lblTitle.setHorizontalAlignment(SwingConstants.CENTER);
		homePanel.add(lblTitle);
		
		lblFooter = new JLabel("<html><div style='text-align: center;'>Big Data Storage System<br>&copy; 2019</div></html>");
		lblFooter.setFont(new Font("Gulim", Font.BOLD, 12));
		lblFooter.setBounds(280, 510, 150, 30);
		lblFooter.setHorizontalAlignment(SwingConstants.CENTER);
		homePanel.add(lblFooter);
	}
	
	public void InsertPanel() {
		JFilePicker filePicker = new JFilePicker("Pick a file", "Browse...");
		FlowLayout flowLayout = (FlowLayout) filePicker.getLayout();
		flowLayout.setVgap(20);
		filePicker.setBounds(0, 198, 684, 68);
		filePicker.setMode(JFilePicker.MODE_OPEN);
		filePicker.addFileTypeFilter(".csv", "CSV Files");
		JFileChooser fileChooser = filePicker.getFileChooser();
		fileChooser.setCurrentDirectory(new File("C:/"));
		insertPanel.add(filePicker);
		
		lblResponse = new JLabel("Response");
		lblResponse.setFont(new Font("Gulim", Font.BOLD, 18));
		lblResponse.setBounds(200, 325, 250, 50);
		lblResponse.setHorizontalAlignment(SwingConstants.CENTER);
		insertPanel.add(lblResponse);

		btnUpload = new JButton("UPLOAD");
		btnUpload.setBounds(275, 275, 100, 30);
		btnUpload.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				System.out.println(filePicker.getSelectedFilePath());
				// call python
				try {
					lblResponse.setText(String.valueOf("Success"));
					
					String prg = "import sys";
					BufferedWriter out = new BufferedWriter(new FileWriter("Preprocess/main_preprocessing.py"));
					out.write(prg);
					out.close();
					Process p = Runtime.getRuntime().exec("python Preprocess/main_preprocessing.py");
					BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
					String ret = in.readLine();
//					System.out.println("value is : "+ret);
				
				} catch (Exception e2) {
					// TODO: handle exception
				}
			}
		});
		insertPanel.add(btnUpload);
	}
	
	public void QueryPanel() {
		tfStartTime = new JFormattedTextField();
		tfStartTime.setFormatterFactory(new DefaultFormatterFactory(new DateFormatter(new SimpleDateFormat("HH:mm"))));
		tfStartTime.setBounds(80, 5, 250, 25);
		tfStartTime.setValue(Calendar.getInstance().getTime());
		queryPanel.add(tfStartTime);
		tfStartTime.setColumns(10);
		
		tfDuration = new JTextField();
		tfDuration.setBounds(80, 35, 250, 25);
		queryPanel.add(tfDuration);
		tfDuration.setColumns(10);
		
		tfEdge = new JTextField();
		tfEdge.setBounds(410, 5, 250, 25);
		queryPanel.add(tfEdge);
		tfEdge.setColumns(10);
		
		lblStartTime = new JLabel("Start time");
		lblStartTime.setBounds(10, 5, 60, 25);
		lblStartTime.setHorizontalAlignment(SwingConstants.RIGHT);
		queryPanel.add(lblStartTime);
		
		lblDuration = new JLabel("Duration");
		lblDuration.setBounds(10, 35, 60, 25);
		lblDuration.setHorizontalAlignment(SwingConstants.RIGHT);
		queryPanel.add(lblDuration);
		
		lblEdge = new JLabel("Edge");
		lblEdge.setBounds(340, 5, 60, 25);
		lblEdge.setHorizontalAlignment(SwingConstants.RIGHT);
		queryPanel.add(lblEdge);
		
		btnSearch = new JButton("QUERY");
		btnSearch.setFont(new Font("Gulim", Font.PLAIN, 12));
		btnSearch.setBounds(284, 70, 100, 30);
		queryPanel.add(btnSearch);
		
		taLatLong = new TextArea();
		taLatLong.setBounds(10, 106, 650, 444);
		taLatLong.setEditable(false);
//        textArea.setLineWrap(true);
//        textArea.setWrapStyleWord(true);
		queryPanel.add(taLatLong);
		
		btnSearch.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (!tfStartTime.getText().equals("") && !tfDuration.getText().equals("") && !tfEdge.getText().equals("")) {
					String hour = tfStartTime.getText().split(":")[0];
					String minute = tfStartTime.getText().split(":")[1];

					Integer quarter = Integer.valueOf(minute) / 15; 
					switch(quarter) {
						case 0:
							minute = "00";
							break;
						case 1:
							minute = "15";
							break;
						case 2:
							minute = "30";
							break;
						case 3:
							minute = "45";
							break;					
					}
					
					String startTime = hour + minute;
					String duration = tfDuration.getText();
					String edge = tfEdge.getText();
					
					selected_edge = new ArrayList<String>();
					taLatLong.setText("");

					//con.QueryST("0015", "10", "23362");
					List<String> taxi = con.QuerySTListTaxi(startTime, duration, edge);
					System.out.println("taxi_id: " + taxi);
					
					for(int i = 0; i < taxi.size(); i++) {

						set = new HashSet<>(selected_edge);
						selected_edge.clear();
						selected_edge.addAll(set);
						
						Recursive(startTime, duration, edge, taxi.get(i), "0");

						System.out.println("selected_edge size: " + selected_edge.size());

						List<Coordinate> coordinate = new ArrayList<Coordinate>();
						// Proses buat dapetin semua latlong yang dilalui
						for(int k = 0; k < selected_edge.size(); k++) {
							List<STTrajectoryEntity> datast = con.QueryLatLong(selected_edge.get(k));
							Set<STTrajectoryEntity> setst = new HashSet<>(datast);
							datast.clear();
							datast.addAll(setst);
							for(STTrajectoryEntity data : datast) {
								coordinate.add(new Coordinate(data.getS_lat(), data.getS_long()));
							}
						}
						
						Set<Coordinate> sets = new HashSet<>(coordinate);
						coordinate.clear();
						coordinate.addAll(sets);
						
						taLatLong.append("Latitude" + "				" + "Longitude" + "\n");
						for(int k = 0; k < coordinate.size(); k++) {
//							System.out.println(coordinate.get(k).getLatitude() + "	" + coordinate.get(k).getLongitude() + "	cross5	red	1	This is a fairly large cross on the map.");
							System.out.println(coordinate.get(k).getLatitude() + "	" + coordinate.get(k).getLongitude());
							taLatLong.append(coordinate.get(k).getLatitude() + "			" + coordinate.get(k).getLongitude() + "\n");
						}
					}
					
//					PApplet.main(new String[] { UnfoldingMaps.class.getName() });
				}
				else {
					JOptionPane.showMessageDialog(null, "All field must be filled!", "Error", JOptionPane.ERROR_MESSAGE);
				}
			}
		});
	}
	
	public void Recursive(String startTime, String duration, String edge, String taxi, String elapse_time) {
		
		String time_spent = "";
		
		if (set.contains(edge)) {
			return;
		}
		else if (Float.valueOf(duration) <= 0 && !edge.equals("0")) {
			return;
		}
		else {
			selected_edge.add(edge);
			set = new HashSet<>(selected_edge);
			selected_edge.clear();
			selected_edge.addAll(set);
			
//			time_spent = con.QuerySTTimeSpent(startTime, taxi, cur_edge);
			time_spent = con.QuerySTTimeSpent(taxi, edge);
			
			elapse_time = String.valueOf(Float.valueOf(elapse_time) + Float.valueOf(time_spent));
			if(Float.valueOf(elapse_time) > 15) {
				startTime = String.valueOf(Integer.valueOf(startTime) + 15);
				if (Integer.valueOf(startTime)%100 >= 60) {
					startTime = String.valueOf(Integer.valueOf(startTime) - 60);
					startTime = String.valueOf(Integer.valueOf(startTime) + 100);
				}
				elapse_time = String.valueOf(Float.valueOf(elapse_time) - 15);
			}
			duration = String.valueOf(Float.valueOf(duration) - Float.valueOf(time_spent));

			List<String> next = con.QueryCon(taxi, edge);
			for (int i = 0; i < next.size(); i++) {
				System.out.println("next_recursive: " + startTime + " " + duration + " " + next.get(i) + " " + taxi + " " + elapse_time);
				Recursive(startTime, duration, next.get(i), taxi, elapse_time);
			}
		}
	}
}
