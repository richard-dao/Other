//Java
public static int[] selectionSort(int[] list) {
		for (int i = 0; i < list.length-1; i++) {
			int min_index = i;
			
			for (int j = i+1; j < list.length; j++) {
				if (list[j] < list[min_index]) {
					min_index = j;
				}
			}
			
			int temp = list[i];
			list[i] = list[min_index];
			list[min_index] = temp;
			
		}
		return list;
		
	}
