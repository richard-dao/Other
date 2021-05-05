//Java

// While-Loop
public static int binarySearch(int[] list, int search) {
		// Returns index of searched element
		int low = 0, high = list.length-1;
		
		while (low <= high) {
			int mid = (high+low)/2;
			if (list[mid] == search) {
				return mid;
			}
			else if (list[mid] < search) {
				low = mid + 1;
			}
			else {
				high = mid - 1;
			}
		}
		return -1;
	}

//For-Loop
public static int binarySearchFor(int[] list, int search) {
		int low = 0, high = list.length-1;
		
		for (;low <= high;) {
			int mid = (high + low)/2;
			if (list[mid] == search) {
				return mid;
			}
			else if (list[mid] < search) {
				low = mid + 1;
			}
			else {
				high = mid - 1;
			}
		}
		return -1;
	}

//Recursive
public static int binarySearchRecursive(int[] list, int low, int high, int search) {
		int mid = (low+high)/2;
		if (list[mid] == search) {
			return mid;
		}
		if (low > high) {
			return -1;
		}
		
		if (list[mid] < search) {
			low = mid + 1;
		}
		else if (list[mid] > search) {
			high = mid - 1;
		}
		return binarySearchRecursive(list, low, high, search); 
		
	}
