package project.bdss;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.SwingConstants;

import processing.core.PApplet;

import javax.swing.JPanel;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JButton;
import javax.swing.JFileChooser;

import java.awt.event.ActionListener;
import java.io.File;
import java.awt.event.ActionEvent;
import java.awt.CardLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import javax.swing.JTextField;

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
	private JTextField tfStartTime;
	private JTextField tfDuration;
	private JTextField tfLatitude;
	private JTextField tfLongitude;

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
	 */
	public Main() {
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
		filePicker.addFileTypeFilter(".txt", "TXT Files");
		JFileChooser fileChooser = filePicker.getFileChooser();
		fileChooser.setCurrentDirectory(new File("C:/"));
		insertPanel.add(filePicker);
		
		btnUpload = new JButton("UPLOAD");
		btnUpload.setBounds(275, 275, 100, 30);
		insertPanel.add(btnUpload);
		
		lblResponse = new JLabel("Response");
		lblResponse.setFont(new Font("Gulim", Font.BOLD, 18));
		lblResponse.setBounds(200, 325, 250, 50);
		lblResponse.setHorizontalAlignment(SwingConstants.CENTER);
		insertPanel.add(lblResponse);
	}
	
	public void QueryPanel() {
		tfStartTime = new JTextField();
		tfStartTime.setBounds(80, 5, 250, 25);
		queryPanel.add(tfStartTime);
		tfStartTime.setColumns(10);
		
		tfDuration = new JTextField();
		tfDuration.setBounds(80, 35, 250, 25);
		queryPanel.add(tfDuration);
		tfDuration.setColumns(10);
		
		tfLatitude = new JTextField();
		tfLatitude.setBounds(410, 5, 250, 25);
		queryPanel.add(tfLatitude);
		tfLatitude.setColumns(10);
		
		tfLongitude = new JTextField();
		tfLongitude.setColumns(10);
		tfLongitude.setBounds(410, 35, 250, 25);
		queryPanel.add(tfLongitude);
		
		JLabel lblStartTime = new JLabel("Start time");
		lblStartTime.setBounds(10, 5, 60, 25);
		lblStartTime.setHorizontalAlignment(SwingConstants.RIGHT);
		queryPanel.add(lblStartTime);
		
		JLabel lblDuration = new JLabel("Duration");
		lblDuration.setBounds(10, 35, 60, 25);
		lblDuration.setHorizontalAlignment(SwingConstants.RIGHT);
		queryPanel.add(lblDuration);
		
		JLabel lblLatitude = new JLabel("Latitude");
		lblLatitude.setBounds(340, 5, 60, 25);
		lblLatitude.setHorizontalAlignment(SwingConstants.RIGHT);
		queryPanel.add(lblLatitude);
		
		JLabel lblLongitude = new JLabel("Longitude");
		lblLongitude.setBounds(340, 35, 60, 25);
		lblLongitude.setHorizontalAlignment(SwingConstants.RIGHT);
		queryPanel.add(lblLongitude);
		
		JButton btnSearch = new JButton("QUERY");
		btnSearch.setFont(new Font("Gulim", Font.PLAIN, 12));
		btnSearch.setBounds(284, 70, 100, 30);
		queryPanel.add(btnSearch);

		btnSearch.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				PApplet.main(new String[] { UnfoldingMaps.class.getName() });
			}
		});
	}
}
