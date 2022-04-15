1. Select a frame (or a few frames) of LiDAR data file, parse the file and visualize the 3D point cloud of that frame.

![image](https://user-images.githubusercontent.com/79803663/163603817-18042c95-c28e-40c2-a67a-8d0fa2d9afa7.png)


2. Perform voxel filter (or box grid filter) to down-sample all the 3D point cloud points to the 3D voxel space points, and visualize the result points.

![image](https://user-images.githubusercontent.com/79803663/163603839-a155d940-8cbb-4e9e-8f4a-57bd4d274aa6.png)


3. Apply RANSAC algorithm (or any others you prefer) to the 3D voxel space points to find a ground plane model.

### Elapsed time for RANSAC algorithm is 0.306283 seconds.

![image](https://user-images.githubusercontent.com/79803663/163603852-60a99e85-710d-458c-b8da-f0eeb9fc0fb2.png)

![image](https://user-images.githubusercontent.com/79803663/163603863-ad15b534-845a-4a81-8a3f-e046a9b8d305.png)

4. Remove all the ground planes points in the 3D voxel space points, visualize all the off-ground points in the 3D.

![image](https://user-images.githubusercontent.com/79803663/163603982-06166ba0-b56d-434b-af01-5054263d99ef.png)

5. Perform a x-y projection to the off-ground points, and get a 2D matrix (you decide what is the element value), and visualize the 2D matrix as an image.

![image](https://user-images.githubusercontent.com/79803663/163604016-20463618-14d1-4719-bfcb-2c0c66aa0a6f.png)


6. Based on the raw point cloud data (Questions 1), which is in Cartesian Coordinate, represent and visualize all the point cloud in 3D of horizontal and vertical angels (converted using Polar Coordinate).

![image](https://user-images.githubusercontent.com/79803663/163604048-4c43c491-303b-4db6-8dec-66954a84316f.png)
![image](https://user-images.githubusercontent.com/79803663/163604074-aa64ef65-9697-47af-aa92-cada6e029186.png)

7. Generate the projected 2D depth image w.r.t horizontal and vertical angels, with intensity value using the distance.

![2D_depth](https://user-images.githubusercontent.com/79803663/163604710-8bc833f0-992b-400a-bbb1-99ff20219cdf.jpg)

![2D_depthim](https://user-images.githubusercontent.com/79803663/163604690-dcb7c213-51fd-4f36-8dd5-c8c2801e23e5.jpg)




