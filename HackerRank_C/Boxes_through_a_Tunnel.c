

struct box
{
	int length;
	int width;
	int height;
};

typedef struct box box;

int get_volume(box b) 
{
	return (b.length*b.width*b.height);
}
int is_lower_than_max_height(box b) 
{
    if(b.height > 40)
    {
        return 0;
    }
    else 
    {
        return 1;
    }
}
